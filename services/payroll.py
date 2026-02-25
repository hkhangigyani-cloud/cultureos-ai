import json

def fetch_payroll_data():
    with open("data/mock_payroll.json") as f:
        return json.load(f)
