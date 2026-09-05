def print_dashboard(state):
    print("\n" + "=" * 44)
    print("           GOVERNMENT STATUS")
    print("=" * 44)
    print(f" Term {state['term']}  |  Turn {state['turn']}/{state['total_turns']}")
    print(f" Treasury:              {state['treasury']:.0f}B")
    print(f" Economy:               {state['economy']}")
    print(f" Employment:            {state['employment']}")
    print(f" Inflation:             {state['inflation']}")
    print(f" Public Trust:          {state['public_trust']}")
    print(f" Public Satisfaction:   {state['public_satisfaction']}")
    print(f" Public Anger:          {state['public_anger']}")
    print(f" Media Pressure:        {state['media_pressure']}")
    print(f" Opposition Strength:   {state['opposition_strength']}")
    print(f" Govt Efficiency:       {state['government_efficiency']}")
    print(f" Institutional Trust:   {state['institutional_trust']}")
    print(f" Corruption Risk:       {state['corruption_risk']}")
    print("=" * 44)


def print_promises(state):
    print("\n--- PROMISE TRACKER ---")
    for p in state["promises"]:
        print(f" {p['id']}: {p['title']}")
        print(f"    Target: {p['target']}  Actual: {p['actual']}  Status: {p['status']}")

