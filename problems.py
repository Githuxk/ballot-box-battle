PROBLEMS = [
    {
        "id": "unemployment",
        "title": "Youth unemployment has reached a critical level.",
        "category": "Economy",
        "options": {
            "A": {
                "label": "Government hiring drive (high cost, fast results)",
                "effects": {"treasury": -400, "employment": 8, "public_satisfaction": 6,
                            "government_efficiency": -2, "promise_progress": {"Economy": 60000}},
            },
            "B": {
                "label": "Private-sector incentives (medium cost, delayed results)",
                "effects": {"treasury": -200, "employment": 3, "economy": 3,
                            "public_satisfaction": 2, "promise_progress": {"Economy": 20000}},
            },
            "C": {
                "label": "Skills training programme (long-term impact)",
                "effects": {"treasury": -150, "employment": 1, "institutional_trust": 2,
                            "promise_progress": {"Economy": 40000}},
            },
            "D": {
                "label": "Do nothing",
                "effects": {"public_anger": 10, "opposition_strength": 6, "public_satisfaction": -5},
            },
        },
    },
    {
        "id": "inflation",
        "title": "Rising prices are squeezing household budgets.",
        "category": "Economy",
        "options": {
            "A": {
                "label": "Increase fuel & food subsidies (costly, popular)",
                "effects": {"treasury": -350, "public_satisfaction": 7, "inflation": -5},
            },
            "B": {
                "label": "Raise interest rates via central bank pressure",
                "effects": {"inflation": -8, "economy": -4, "public_satisfaction": -2},
            },
            "C": {
                "label": "Targeted relief for lowest-income households",
                "effects": {"treasury": -150, "public_satisfaction": 4, "inflation": -2},
            },
            "D": {
                "label": "Do nothing, let the market correct",
                "effects": {"public_anger": 8, "public_satisfaction": -6},
            },
        },
    },
    {
        "id": "education_quality",
        "title": "Schools report severe teacher shortages and overcrowding.",
        "category": "Education",
        "options": {
            "A": {
                "label": "Emergency teacher recruitment drive",
                "effects": {"treasury": -250, "institutional_trust": 3,
                            "promise_progress": {"Education": 60}},
            },
            "B": {
                "label": "Digital learning programme (cheaper, slower results)",
                "effects": {"treasury": -100, "government_efficiency": 2,
                            "promise_progress": {"Education": 25}},
            },
            "C": {
                "label": "Partner with private schools for overflow capacity",
                "effects": {"treasury": -50, "public_satisfaction": -2,
                            "promise_progress": {"Education": 15}},
            },
            "D": {
                "label": "Delay the issue to next budget cycle",
                "effects": {"public_anger": 6, "media_pressure": 6},
            },
        },
    },
    {
        "id": "healthcare_shortage",
        "title": "Rural hospitals are critically understaffed.",
        "category": "Healthcare",
        "options": {
            "A": {
                "label": "Fund 100 new rural clinics immediately",
                "effects": {"treasury": -400, "public_trust": 5,
                            "promise_progress": {"Healthcare": 100}},
            },
            "B": {
                "label": "Mobile health units as a stopgap",
                "effects": {"treasury": -150, "public_satisfaction": 3,
                            "promise_progress": {"Healthcare": 30}},
            },
            "C": {
                "label": "Incentivize doctors to relocate rurally",
                "effects": {"treasury": -100, "government_efficiency": 2,
                            "promise_progress": {"Healthcare": 20}},
            },
            "D": {
                "label": "No action this cycle",
                "effects": {"public_anger": 9, "public_trust": -4},
            },
        },
    },
    {
        "id": "infrastructure_roads",
        "title": "Deteriorating roads are causing accidents and delays.",
        "category": "Infrastructure",
        "options": {
            "A": {
                "label": "Major national road repair programme",
                "effects": {"treasury": -450, "economy": 3,
                            "promise_progress": {"Infrastructure": 3000}},
            },
            "B": {
                "label": "Repair only the worst-hit regions",
                "effects": {"treasury": -180, "public_satisfaction": 2,
                            "promise_progress": {"Infrastructure": 1200}},
            },
            "C": {
                "label": "Public-private partnership for tolled repairs",
                "effects": {"treasury": -50, "public_satisfaction": -3,
                            "promise_progress": {"Infrastructure": 1500}},
            },
            "D": {
                "label": "Postpone repairs",
                "effects": {"public_anger": 7, "opposition_strength": 4},
            },
        },
    },
    {
        "id": "agriculture_crisis",
        "title": "Farmers are protesting over crop prices and water shortages.",
        "category": "Agriculture",
        "options": {
            "A": {
                "label": "Guarantee minimum crop prices",
                "effects": {"treasury": -300, "public_trust": 5,
                            "promise_progress": {"Agriculture": 300000}},
            },
            "B": {
                "label": "Invest in irrigation infrastructure",
                "effects": {"treasury": -250, "economy": 2,
                            "promise_progress": {"Agriculture": 200000}},
            },
            "C": {
                "label": "Emergency drought relief fund",
                "effects": {"treasury": -150, "public_satisfaction": 4,
                            "promise_progress": {"Agriculture": 80000}},
            },
            "D": {
                "label": "Refer the issue to a committee",
                "effects": {"public_anger": 9, "media_pressure": 5},
            },
        },
    },
    {
        "id": "bureaucracy_delay",
        "title": "Citizens report months-long delays for basic government paperwork.",
        "category": "Governance",
        "options": {
            "A": {
                "label": "Full digitization of public services",
                "effects": {"treasury": -300, "government_efficiency": 8,
                            "promise_progress": {"Governance": 30}},
            },
            "B": {
                "label": "Hire additional administrative staff",
                "effects": {"treasury": -150, "government_efficiency": 4,
                            "promise_progress": {"Governance": 10}},
            },
            "C": {
                "label": "Set service-delivery deadlines with penalties",
                "effects": {"government_efficiency": 3, "institutional_trust": 2,
                            "promise_progress": {"Governance": 8}},
            },
            "D": {
                "label": "Ignore the complaints",
                "effects": {"public_anger": 6, "institutional_trust": -4},
            },
        },
    },
    {
        "id": "court_backlog",
        "title": "The justice system faces a massive case backlog.",
        "category": "Law & Justice",
        "options": {
            "A": {
                "label": "Fund new fast-track courts",
                "effects": {"treasury": -300, "institutional_trust": 6,
                            "promise_progress": {"Law & Justice": 20}},
            },
            "B": {
                "label": "Recruit additional judges",
                "effects": {"treasury": -200, "institutional_trust": 4,
                            "promise_progress": {"Law & Justice": 12}},
            },
            "C": {
                "label": "Promote mediation for minor disputes",
                "effects": {"treasury": -50, "government_efficiency": 2,
                            "promise_progress": {"Law & Justice": 6}},
            },
            "D": {
                "label": "No reform this term",
                "effects": {"public_anger": 5, "institutional_trust": -3},
            },
        },
    },
    {
        "id": "corruption_scandal",
        "title": "An investigation has found wrongdoing inside your own administration.",
        "category": "Governance",
        "options": {
            "A": {
                "label": "Expose it publicly and remove those responsible",
                "effects": {"institutional_trust": 8, "public_trust": 5,
                            "corruption_risk": -10, "opposition_strength": 6},
            },
            "B": {
                "label": "Quietly manage it internally",
                "effects": {"public_satisfaction": 3, "corruption_risk": 8,
                            "institutional_trust": -6},
            },
            "C": {
                "label": "Launch a full independent investigation",
                "effects": {"institutional_trust": 6, "media_pressure": 8,
                            "corruption_risk": -6, "public_anger": 3},
            },
        },
    },
]

