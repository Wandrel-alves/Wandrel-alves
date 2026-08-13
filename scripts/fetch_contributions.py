import os
import json
import requests
from bs4 import BeautifulSoup

# O NOME DO USUÁRIO PRECISA ESTAR ENTRE ASPAS DUPLAS OU SIMPLES " "
USERNAME = "Wandrel-alves" 

def fetch_data():
    url = f"https://github.com/users/{USERNAME}/contributions"
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"Erro ao acessar {url}: Status {res.status_code}")

    soup = BeautifulSoup(res.text, 'html.parser')
    days = soup.find_all('td', class_='ContributionCalendar-day')
    
    contrib_data = []
    for day in days:
        date = day.get('data-date')
        level = day.get('data-level', '0')
        if date:
            contrib_data.append({"date": date, "level": int(level)})

    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(contrib_data, f, indent=2)
        
    print(f"Dados salvos com sucesso ({len(contrib_data)} dias encontrados).")

if __name__ == "__main__":
    fetch_data()