# 9. zadatak
# uklanjanje duplikata samo pomoću liste

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
nova_lista = []

def ukloni_duplikate(lista): 
    for vrijednost in lista:
        if vrijednost not in nova_lista: 
            nova_lista.append(vrijednost)
    return nova_lista

print(ukloni_duplikate(lista)) 

# uklanjanje pomoću skupa
def ukloni_duplikate(lista): 
    pomocni_set = set(lista)
    return list(pomocni_set)

print(ukloni_duplikate(lista))
