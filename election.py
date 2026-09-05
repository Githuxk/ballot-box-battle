def run_election(state):
    print("\n" + "#" * 44)
    print("             ELECTION DAY")
    print("#" * 44)

    groups = {
        "Youth": (state["employment"] + state["public_satisfaction"]) / 2,
        "Workers": (state["economy"] + state["employment"]) / 2,
        "Farmers": (state["economy"] + state["public_trust"]) / 2,
        "Businesses": state["economy"] - state["inflation"] / 2 + 25,
        "Urban": (state["public_satisfaction"] + state["institutional_trust"]) / 2,
        "Rural": (state["public_trust"] + state["economy"]) / 2,
    }

    total = 0
    print("\nSUPPORT BY GROUP:")
    for group, score in groups.items():
        score = max(0, min(100, score))
        total += score
        print(f"  {group:12s} {score:.0f}%")

    overall = total / len(groups)
    print(f"\nOVERALL SUPPORT: {overall:.0f}%")

    if overall >= 50:
        print("\nRESULT: RE-ELECTED")
        return True
    else:
        print("\nRESULT: DEFEATED")
        return False

