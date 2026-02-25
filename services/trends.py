import requests
from bs4 import BeautifulSoup

def fetch_hr_trends():
    try:
        url = "https://hbr.org/topic/human-resources"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []
        for h in soup.find_all("h3")[:5]:
            headlines.append(h.text.strip())

        return {"trends": headlines}
    except:
        return {"trends": ["AI in HR transformation", "Workforce upskilling acceleration"]}
