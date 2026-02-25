import json

def analyze_skill_gaps():
    with open("data/mock_employees.json") as f:
        employees = json.load(f)

    gaps = []
    for emp in employees:
        if emp["performance_score"] <= 3:
            gaps.append({
                "employee": emp["name"],
                "recommendation": "Leadership & capability development plan"
            })
    return gaps
