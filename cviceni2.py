"""""
if __name__ == "__main__":
    seznam = [100, 5, 3, 21]

    seznam[2] *= 2

    seznam.append(55)

    seznam.sort()

    seznam.reverse()

    print(seznam)


def vrat_treti_prvek(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None

def prumer(cisla):
    if not cisla:
        return 0.0
    return sum(cisla) / len(cisla)

if __name__ == "__main__":
    cisla = [1, 2, 3, 4, 5]
    print(f"Průměr je: {prumer(cisla)}")  # vypise 3.0

    if __name__ == "__main__":
        #prace_se_seznamem()
        x=[1, 2]
        print(vrat_treti_prvek(x)) # none
        
        
        y=[12,34,56,78]
        print(vrat_treti_prvek(y)) # 56
"""
     

def prumer(znamky):
    return sum(znamky) / len(znamky)

def naformatuj_text(zak):
    jmeno = zak["jmeno"]
    prijmeni = zak["prijmeni"]
    vek = zak["rocnik"]
    obor = zak["obor"]
    zaokrouhleno = round(prumer(zak["znamky"]), 2) # zaokrouhleni na 2 desetinna mista
    text = f"Student: {jmeno} {prijmeni}, Vek: {vek}, Obor: {obor}, Prumer: {zaokrouhleno}"
    return text

if __name__ == "__main__":
    
    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "rocnik": 22,
        "znamky": [1, 2, 3, 1, 2, 1]
        }

    student["obor"] = "Informatika"
    student["rocnik"] += 1

    print(naformatuj_text(student))  # vypise "Student Jan Novak, Vek 23, Obor: Informatika, Prumer: 1.6666666666666667"""




