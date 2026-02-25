from fastapi import FastAPI
from services.trends import fetch_hr_trends
from services.payroll import fetch_payroll_data
from services.lnd import analyze_skill_gaps
from core.ai_engine import generate_strategy

app = FastAPI(title="CultureOS AI")

@app.get("/")
def home():
    return {"status": "CultureOS AI is running"}

@app.post("/strategy")
def strategy(query: str):
    trends = fetch_hr_trends()
    payroll = fetch_payroll_data()
    skill_gaps = analyze_skill_gaps()

    response = generate_strategy(query, trends, payroll, skill_gaps)

    return {"recommendation": response}
