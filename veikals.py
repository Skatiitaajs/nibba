cenradis = {
    "Zobens": 100,
    "Vairogs": 80,
    "Loks": 120
}

def pirkt_lietu(nosaukums):
    if nosaukums in cenradis:
        return cenradis[nosaukums]
    else:
        return 0

prece = input("Ievadi priekšmetu: ")

cena = pirkt_lietu(prece)

if cena > 0:
    print("Cena ir:", cena)
else:
    print("Tāda priekšmeta nav.")