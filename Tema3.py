meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

def proceseaza_comenzi(studenti, comenzi, tavi):
    while studenti and comenzi and tavi:
        student = studenti.pop(0)  # elimina studentul din coada
        comanda = comenzi.pop(0)    # elimina comanda din coada
        tava = tavi.pop()            # elimina tava din stiva
        istoric_comenzi.append(comanda)  # actualizează istoricul

        print(f"{student} a comandat {comanda}.")

proceseaza_comenzi(studenti, comenzi, tavi)

def inventar(meniu, istoric_comenzi, tavi):
    from collections import Counter

    comenzi_counter = Counter(istoric_comenzi)
    papanasi_disponibili = meniu.count('papanasi')
    ceafa_disponibili = meniu.count('ceafa')
    guias_disponibili = meniu.count('guias')
  
    print(f"S-au comandat {comenzi_counter['guias']} guias, {comenzi_counter['ceafa']} ceafa, {comenzi_counter['papanasi']} papanasi.")
    print(f"Mai sunt {len(tavi)} tavi.")
    print(f"Mai este ceafa: {ceafa_disponibili > 0}.")
    print(f"Mai sunt papanasi: {papanasi_disponibili > 0}.")
    print(f"Mai sunt guias: {guias_disponibili > 0}.")

inventar(meniu, istoric_comenzi, tavi)

def financiare(istoric_comenzi, preturi):
    total = 0
    preturi_produse = {produs: pret for produs, pret in preturi}

    for comanda in istoric_comenzi:
        total += preturi_produse[comanda]

    produse_mici = [produs for produs, pret in preturi if pret <= 7]

    print(f"Cantina a încasat: {total} lei.")
    print(f"Produse care costă cel mult 7 lei: {[[produs, preturi_produse[produs]] for produs in produse_mici]}.")

financiare(istoric_comenzi, preturi)
