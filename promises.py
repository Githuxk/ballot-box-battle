PROMISE_CATALOG = {
    "1": {"category": "Economy", "title": "Create 500,000 jobs", "target": 500000, "deadline": 6},
    "2": {"category": "Education", "title": "Build 200 new schools", "target": 200, "deadline": 8},
    "3": {"category": "Healthcare", "title": "Open 100 rural clinics", "target": 100, "deadline": 8},
    "4": {"category": "Infrastructure", "title": "Repair 5,000km of roads", "target": 5000, "deadline": 6},
    "5": {"category": "Agriculture", "title": "Irrigate 1 million acres", "target": 1000000, "deadline": 8},
    "6": {"category": "Governance", "title": "Digitize 50 public services", "target": 50, "deadline": 6},
    "7": {"category": "Law & Justice", "title": "Clear 30% of court backlog", "target": 30, "deadline": 8},
}


def choose_promises():
    print("\n=== CAMPAIGN: CHOOSE YOUR PROMISES ===")
    print("Pick 5 promises to run your campaign on.\n")
    for key, p in PROMISE_CATALOG.items():
        print(f"  [{key}] ({p['category']}) {p['title']}")

    chosen_ids = []
    while len(chosen_ids) < 5:
        pick = input(f"\nPick promise #{len(chosen_ids) + 1} of 5 (enter number): ").strip()
        if pick in PROMISE_CATALOG and pick not in chosen_ids:
            chosen_ids.append(pick)
        else:
            print("Invalid choice or already picked. Try again.")

    promises = []
    for i, pid in enumerate(chosen_ids):
        p = PROMISE_CATALOG[pid]
        promises.append({
            "id": f"P{i + 1:03d}",
            "category": p["category"],
            "title": p["title"],
            "target": p["target"],
            "actual": 0,
            "deadline": p["deadline"],
            "status": "In progress",
        })
    return promises

