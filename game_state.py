import json
import os

SAVE_FILE = "save_game.json"

DEFAULT_STATE = {
    "term": 1,
    "turn": 1,
    "total_turns": 8,
    "treasury": 8200,          # in billions of currency units
    "economy": 60,
    "employment": 55,
    "inflation": 55,
    "public_trust": 55,
    "public_satisfaction": 55,
    "public_anger": 25,
    "media_pressure": 30,
    "opposition_strength": 35,
    "government_efficiency": 55,
    "institutional_trust": 65,
    "corruption_risk": 25,
    "promises": [],
    "history": [],
    "game_over": False,
}


def new_game():
    state = dict(DEFAULT_STATE)
    state["promises"] = []
    state["history"] = []
    return state


def save_game(state):
    with open(SAVE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return None


def clamp(value, low=0, high=100):
    return max(low, min(high, value))

