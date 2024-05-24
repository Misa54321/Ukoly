import json
import requests


# Zisk dat z API
response = requests.get('https://cat-fact.herokuapp.com/facts?animal_type=cat&amount=10')
data = response.json()
 
# Vypis pouze casti s textem, ktery nas zajima
text_facts = [fact["text"] for fact in data]

# Zisk ocislovaneho seznamu
for i, fact in enumerate(text_facts, 1):
    print(f"{i}. {fact}")

# Tvorba souboru s fakty
with open('kocici_fakta.json', mode='w', encoding='utf-8') as output_file:
    json.dump(data, output_file, indent=4)

# Zkouska spadnitu programu pri zadani timeoutu
try:
    response = requests.get('https://cat-fact.herokuapp.com/facts?animal_type=cat&amount=10', timeout=0.001)
    data = response.json()
except requests.Timeout:
    print("Jste prilis nedockavi.")