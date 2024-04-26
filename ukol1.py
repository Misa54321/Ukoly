# Trida zvire
class Zvire:
    def __init__(self, jmeno, druh, vaha):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    def __str__(self):
        return(f'{self.jmeno} je druhu {self.druh} a vazi {self.vaha} kg.')
    def export_to_dict(self):
        return {
            'jmeno': self.jmeno,
            'druh': self.druh,
            'vaha': self.vaha
        }
# reprezentace zvířete jako slovník
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
pavouk_export = pavouk.export_to_dict()
print(pavouk)
print(pavouk_export)

# # Seznam slovníků
zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

# # List pro ukládání objektů typu Zvire
zvirata = []

# # Vytvoření objektů typu Zvire z každého slovníku a přidání do listu zvirata
for zvire_dict in zvirata_dict:
    zvire = Zvire(zvire_dict['jmeno'], zvire_dict['druh'], zvire_dict['vaha'])
    zvirata.append(zvire)

# # Výpis listu obsahujících objekty typu Zvire
for zvire in zvirata:
    print(f"Jméno: {zvire.jmeno}, Druh: {zvire.druh}, Váha: {zvire.vaha} kg")

class Zamestnanec:
    def __init__(self, cele_jmeno:str, rocni_plat:int, pozice:str):
        self.cele_jmeno=cele_jmeno
        self.rocni_plat=rocni_plat
        self.pozice=pozice

    def __str__(self):
        return(f'{self.cele_jmeno} ma rocni plat {self.rocni_plat} a pracuje na pozici {self.pozice}.')
    
    def ziskej_inicialy(self):
        jmena = self.cele_jmeno.split()
        if len(jmena) == 2:
            inicialy = f"{jmena[0][0].upper()}.{jmena[1][0].upper()}."
            return inicialy
        else:
            return None
        
zamestnanec=Zamestnanec('Klara Husova', 500_000, 'osetrovatelka')
print(zamestnanec)
print(f"Inicialy: {zamestnanec.ziskej_inicialy()}")

# seznam slovniku
zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
] 
#List pro ukládání objektů typu zamestanec
zamestnanci = []

for zamestnanec_dict in zamestnanci_dict:
    zamestnanec = Zamestnanec(zamestnanec_dict['cele_jmeno'], zamestnanec_dict['rocni_plat'], zamestnanec_dict['pozice'])
    zamestnanci.append(zamestnanec)

# Výpis listu obsahujících objekty typu zamestanec
for zamestnanec in zamestnanci:
    print(f"Cele jméno: {zamestnanec.cele_jmeno}, Rocni plat: {zamestnanec.rocni_plat}, Pozice: {zamestnanec.pozice}")

# trida reditel
class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno:str, rocni_plat:int, oblibene_zvire):
        super().__init__(cele_jmeno, rocni_plat, 'Reditel')
        self.oblibene_zvire = oblibene_zvire

zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
print(f'Reditel se jmenuje {reditel.cele_jmeno}, jeho rocni plat je {reditel.rocni_plat} a jeho oblibene zvire je {reditel.oblibene_zvire}.')

# trida zoo
class Zoo:
    def __init__(self, jmeno, adresa, reditel, zamestnanci, zvirata):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata
    def vaha_vsech_zvirat_v_zoo(self):
        celkova_vaha = sum(zvire.vaha for zvire in self.zvirata)
        return celkova_vaha
    
    def mesicni_naklady_na_zamestnance(self):
        mesicni_naklady = sum(zamestnanec.rocni_plat / 12 for zamestnanec in self.zamestnanci)
        mesicni_naklady += self.reditel.rocni_plat / 12
        return mesicni_naklady

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci, zvirata)

print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())
