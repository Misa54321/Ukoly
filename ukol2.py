import sys
import json
import requests

# Pekne reseni!
# Chvalim:
#   - strucnost, citelnost, vysvetlujici komentare
#   - sikovne pouziti enumerate s parametrem `start`
#   - zajimave pouziti slovniku
# Par podnetu k zamysleni:
#   - Ktere hodnoty v kodu by bylo vhodne definovat jako konstanty?
#   - Seznam prochazime dvakrat (1. vytazeni 'text' a ocislovani. 2. tvorba seznamu pro zapis); dalo by se zaridit, aby byl pruchod seznamem jen jeden?
#   - Pro jednotlive kroky (ne nutne vsechny) by se nabizelo pouziti funkci.


# Zisk dat z API
try:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=5)
    data = response.json()
except requests.Timeout:
    print("Jste prilis nedockavi.")
    # Try blok staci kolem vlastniho pozadavku. Lepe tak oddelime jednotlive kroky programu
    #   (1. ziskani dat, 2. transformace dat a 3. zapis dat).
    # Nicmene v pripade vyjimky chceme tady program ukoncit.
    sys.exit(1)
 
# (Kvuli citelnosti byva zvykem odsazovat komentare stejne jako okolni kod.)
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
