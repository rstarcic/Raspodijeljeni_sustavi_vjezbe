# 8. zadatak

lista = [1,2,3,4,5,6,7,8,9,10]

def filtriraj_parne(lista):
    a = []
    for num in lista:
        if num % 2 == 0:
            a.append(num)
    return a
    
print(filtriraj_parne(lista))
