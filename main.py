import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.metrics import dp

from game_state import new_game, save_game, load_game, clamp
from promises import PROMISE_CATALOG, make_promise
from problems import PROBLEMS
from media import generate_headline
from election import evaluate_election


def apply_effects(state, effects):
    for key, val in effects.items():
        if key == "promise_progress":
            for cat, amount in val.items():
                for p in state["promises"]:
                    if p["category"] == cat:
                        p["actual"] += amount
                        if p["actual"] >= p["target"]:
                            p["status"] = "Completed"
            continue
        if key == "treasury":
            state["treasury"] = state["treasury"] + val
            continue
        if key in state and isinstance(state[key], (int, float)):
            state[key] = clamp(state[key] + val)


class PromiseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected = []
        self.layout = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(6))
        self.add_widget(self.layout)

    def on_pre_enter(self, *args):
        self.build_ui()

    def build_ui(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(
            text="CHOOSE 5 CAMPAIGN PROMISES",
            size_hint_y=None, height=dp(40), bold=True))
        self.layout.add_widget(Label(
            text=f"Selected: {len(self.selected)}/5",
            size_hint_y=None, height=dp(30)))

        scroll = ScrollView()
        grid = GridLayout(cols=1, size_hint_y=None, spacing=dp(6))
        grid.bind(minimum_height=grid.setter("height"))

        for pid, p in PROMISE_CATALOG.items():
            label = f"[{p['category']}] {p['title']}"
            btn = Button(text=label, size_hint_y=None, height=dp(60),
                         disabled=pid in self.selected)
            btn.bind(on_release=lambda inst, pid=pid: self.select(pid))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        self.layout.add_widget(scroll)

        if len(self.selected) == 5:
            confirm = Button(text="START GOVERNMENT", size_hint_y=None, height=dp(60))
            confirm.bind(on_release=self.confirm)
            self.layout.add_widget(confirm)

    def select(self, pid):
        if pid not in self.selected and len(self.selected) < 5:
            self.selected.append(pid)
            self.build_ui()

    def confirm(self, *args):
        app = App.get_running_app()
        state = new_game()
        state["promises"] = [make_promise(pid, i) for i, pid in enumerate(self.selected)]
        app.state = state
        save_game(state)
        self.selected = []
        app.sm.current = "game"
        app.sm.get_screen("game").reset_and_start()


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.used_problem_ids = []
        self.current_problem = None
        self.layout = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(6))
        self.add_widget(self.layout)

    def reset_and_start(self):
        self.used_problem_ids = []
        self.start_turn()

    def start_turn(self):
        app = App.get_running_app()
        state = app.state
        self.layout.clear_widgets()

        dash = (
            f"Term {state['term']}   Turn {state['turn']}/{state['total_turns']}\n"
            f"Treasury: {state['treasury']:.0f}B\n"
            f"Economy {state['economy']}  Employment {state['employment']}  "
            f"Inflation {state['inflation']}\n"
            f"Trust {state['public_trust']}  Satisfaction {state['public_satisfaction']}  "
            f"Anger {state['public_anger']}\n"
            f"Media {state['media_pressure']}  Opposition {state['opposition_strength']}\n"
            f"Efficiency {state['government_efficiency']}  "
            f"Inst.Trust {state['institutional_trust']}  "
            f"Corruption {state['corruption_risk']}"
        )
        self.layout.add_widget(Label(text=dash, size_hint_y=None, height=dp(170)))

        promises_text = "\n".join(
            f"{p['id']}: {p['title']} ({p['actual']}/{p['target']}) [{p['status']}]"
            for p in state["promises"]
        )
        promises_scroll = ScrollView(size_hint_y=None, height=dp(90))
        promises_label = Label(text=promises_text, size_hint_y=None, height=dp(150))
        promises_scroll.add_widget(promises_label)
        self.layout.add_widget(promises_scroll)

        if state["public_anger"] >= 75:
            self.layout.add_widget(Label(
                text="!!! PROTESTS IN MAJOR CITIES !!!",
                color=(1, 0.3, 0.3, 1), size_hint_y=None, height=dp(30)))

        available = [p for p in PROBLEMS if p["id"] not in self.used_problem_ids]
        if not available:
            self.used_problem_ids = []
            available = PROBLEMS
        problem = random.choice(available)
        self.used_problem_ids.append(problem["id"])
        self.current_problem = problem

        self.layout.add_widget(Label(
            text=problem["title"], size_hint_y=None, height=dp(50), bold=True))

        for key in sorted(problem["options"].keys()):
            opt = problem["options"][key]
            btn = Button(text=f"[{key}] {opt['label']}", size_hint_y=None, height=dp(70))
            btn.bind(on_release=lambda inst, key=key: self.choose(key))
            self.layout.add_widget(btn)

    def choose(self, key):
        app = App.get_running_app()
        state = app.state
        problem = self.current_problem
        picked = problem["options"][key]
        apply_effects(state, picked["effects"])
        state["history"].append(f"Turn {state['turn']}: {problem['title']} -> chose {key}")

        headline = "\n\n".join(generate_headline(state, problem, key, picked))
        popup = Popup(title="MEDIA REACTION", content=Label(text=headline), size_hint=(0.9, 0.5))

        state["turn"] += 1
        save_game(state)

        def proceed(*a):
            if state["turn"] > state["total_turns"]:
                app.sm.current = "election"
                app.sm.get_screen("election").show_results()
            else:
                self.start_turn()

        popup.bind(on_dismiss=proceed)
        popup.open()


class ElectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(8))
        self.add_widget(self.layout)

    def show_results(self):
        app = App.get_running_app()
        state = app.state
        result = evaluate_election(state)
        self.layout.clear_widgets()

        self.layout.add_widget(Label(
            text="ELECTION DAY", size_hint_y=None, height=dp(50), bold=True))
        for group, score in result["group_scores"].items():
            self.layout.add_widget(Label(
                text=f"{group}: {score:.0f}%", size_hint_y=None, height=dp(30)))

        self.layout.add_widget(Label(
            text=f"OVERALL: {result['overall']:.0f}%",
            size_hint_y=None, height=dp(40), bold=True))
        outcome = "RE-ELECTED" if result["won"] else "DEFEATED"
        self.layout.add_widget(Label(
            text=outcome, size_hint_y=None, height=dp(50), bold=True))

        state["game_over"] = True
        if result["won"]:
            state["term"] += 1
            state["turn"] = 1
            state["game_over"] = False
        save_game(state)

        btn = Button(
            text="NEXT TERM" if result["won"] else "NEW GOVERNMENT",
            size_hint_y=None, height=dp(60))
        btn.bind(on_release=self.restart)
        self.layout.add_widget(btn)

    def restart(self, *args):
        app = App.get_running_app()
        if app.state.get("game_over"):
            app.sm.current = "promises"
        else:
            app.sm.current = "game"
            app.sm.get_screen("game").reset_and_start()


class BallotBoxBattleApp(App):
    def build(self):
        self.title = "The Ballot Box Battle"
        self.sm = ScreenManager()
        self.sm.add_widget(PromiseScreen(name="promises"))
        self.sm.add_widget(GameScreen(name="game"))
        self.sm.add_widget(ElectionScreen(name="election"))

        loaded = load_game()
        if loaded and not loaded.get("game_over") and loaded.get("promises"):
            self.state = loaded
            self.sm.current = "game"
            self.sm.get_screen("game").reset_and_start()
        else:
            self.state = new_game()
            self.sm.current = "promises"

        return self.sm


if __name__ == "__main__":
    BallotBoxBattleApp().run()

