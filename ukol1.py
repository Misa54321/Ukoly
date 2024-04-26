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

# # Example usage
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
pavouk_export = pavouk.export_to_dict()

# # Assertions to test the exported dictionary
assert pavouk_export['jmeno'] == 'Adolf'
assert pavouk_export['druh'] == 'Tarantule Velká'
assert pavouk_export['vaha'] == 0.1

# # Printing the exported dictionary
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
# for zvire in zvirata:
#     print(f"Jméno: {zvire.jmeno}, Druh: {zvire.druh}, Váha: {zvire.vaha} kg")

class Zamestnanec:
    def __init__(self, cele_jmeno:str, rocni_plat:int, pozice:str):
        self.cele_jmeno=cele_jmeno
        self.rocni_plat=rocni_plat
        self.pozice=pozice
    def __str__(self):
        return(f'{self.cele_jmeno} ma rocni plat {self.rocni_plat} a pracuje na pozici {self.pozice}.')
    def ziskej_inicialy(self):
        rozdeleno=self.cele_jmeno.split(' ')
        inicialy=rozdeleno[0][0] + '.' + rozdeleno[1][0] + '.' 
        return inicialy

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

# Výpis listu obsahujících objekty typu Zvire
for zamestnanec in zamestnanci:
    print(f"Cele jméno: {zamestnanec.cele_jmeno}, Rocni plat: {zamestnanec.rocni_plat}, Pozice: {zamestnanec.pozice}")

class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno:str, rocni_plat:int, oblibene_zvire):
        super().__init__(cele_jmeno, rocni_plat, 'Reditel')
        self.oblibene_zvire = oblibene_zvire

zvire = Zvire('Adolf', 'Tarantule Velká', 0.1)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)
print(reditel)


class Zoo:
    