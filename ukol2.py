import json
import requests

# Zisk dat z API
try:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=0.001)
    data = response.json()
 
# Vypis pouze casti s textem, ktery nas zajima
    text_facts = {f"{i}": fact["text"] for i, fact in enumerate(data, 1)}

# Výpis očíslovaných faktů
    cat_facts = []
    for i, fact in text_facts.items():
        cat_facts.append(f"{i}. {fact}")

    print(cat_facts)

# Tvorba souboru s očíslovanými fakty
    with open('kocici_fakta.json', mode='w', encoding='utf-8') as output_file:
        json.dump(cat_facts, output_file, indent=4)

except requests.Timeout:
    print("Jste prilis nedockavi.")