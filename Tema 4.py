import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

print("Bine ai venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit este: " + " ".join(progres))
print(f"Începi cu {incercari_ramase} încercări.\n")

while incercari_ramase > 0 and "_" in progres:
    litera = input("Introdu o literă: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Eroare! Te rog să introduci o literă validă.\n")
        continue

    if litera in litere_incercate:
        print(f"Ai mai încercat litera '{litera}'. Te rog să încerci altă literă.\n")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print("Litera se află în cuvânt!\n")
    else:
        incercari_ramase -= 1
        print(f"Litera nu se află în cuvânt. Ai {incercari_ramase} încercări rămase.\n")

    print("Cuvântul de ghicit este: " + " ".join(progres))
    print(f"Literele încercate: {', '.join(litere_incercate)}\n")

if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul: " + cuvant_de_ghicit)
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
