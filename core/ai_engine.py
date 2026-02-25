from openai import OpenAI
from config import OPENAI_API_KEY
from core.prompts import SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_strategy(query, trends, payroll, skill_gaps):

    context = f"""
    {SYSTEM_PROMPT}

    Live HR Trends: {trends}
    Payroll Data: {payroll}
    Skill Gaps: {skill_gaps}

    Strategic Question: {query}
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "system", "content": context}],
        temperature=0.3
    )

    return response.choices[0].message.content
