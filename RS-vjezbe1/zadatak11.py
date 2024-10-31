# 11. zadatak - Napišite funkciju koja prima listu brojeva i vraća rječnik s dvije liste: jedna za parne brojeve, a druga za neparne brojeve.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def grupiraj_po_paritetu(lista):
    parni_brojevi = []
    neparni_brojevi = []
    for element in lista:
        if(element % 2 == 0):
            parni_brojevi.append(element)
        else:
            neparni_brojevi.append(element)
    return {'parni': parni_brojevi, 'neparni': neparni_brojevi}

print(grupiraj_po_paritetu(lista))   
