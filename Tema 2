import string
text = """Guvernul României a anunțat noi măsuri pentru reducerea cheltuielilor bugetare în următoarea perioadă.
Aceste măsuri includ reducerea unor subvenții și creșterea taxelor pentru anumite categorii."""
mid_index = len(text) // 2
prima_parte = text[:mid_index]
a_doua_parte = text[mid_index:]
prima_parte = prima_parte.upper().strip()  
a_doua_parte = a_doua_parte[::-1]            
a_doua_parte = a_doua_parte.capitalize()      
a_doua_parte = a_doua_parte.translate(str.maketrans('', '', string.punctuation))
rezultat = prima_parte + " " + a_doua_parte   
print("Rezultatul prelucrării textului:")
print(rezultat)
