# 13. zadatak 
# a)  Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda
# b) Funkcija koja n-torku s maksimalnim i minimalnim elementom liste, bez korištenja ugrađenih funkcija max() i min() .
# c) Funkcija presjek koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa.

# a)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def return_tuple(lista): return (lista[0], lista[-1]) if lista else print("Nema liste") 

print(return_tuple(lista))

# b)
def min_and_max(lista): 
    min_elem = lista[0]
    max_elem = lista[0]
    for item in lista:
        if(item < min_elem):
            min_elem = item
        if(item > max_elem):
            max_elem = item
    return (min_elem, max_elem) 

print(min_and_max(lista))

# c)
setA = {"Apple", "Banana", "Plum", "Watermelon", "Strawberry"}
setB = {"Blueberry", "Raspberry", "Watermelon", "Strawberry"}

def set_intersection(setA, setB):
    setC = setA.intersection(setB)
    return setC

print(set_intersection(setA, setB))