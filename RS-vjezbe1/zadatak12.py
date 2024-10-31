# 12. zadatak - Napišite funkciju koja prima rječnik i vraća novi rječnik u kojem su ključevi i vrijednosti zamijenjeni
moj_dict = {
    "ime": "Roberta",
    "prezime": "Starčić",
    "dob": 22
}
novi_dict = {}

def izmijenjeni_dict(dictionary):
    for kljuc, vrijednost in dictionary.items():
        novi_dict[vrijednost] = kljuc
    return novi_dict

print(izmijenjeni_dict(moj_dict))