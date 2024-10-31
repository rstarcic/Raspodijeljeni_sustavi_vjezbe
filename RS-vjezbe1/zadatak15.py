# 15. zadatak - Napišite funkciju count_vowels_consonants() koja prima string i vraća rječnik s brojem samoglasnika i brojem suglasnika u tekstu

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def count_vowels_consonants(tekst):
    vowelsCounter = 0
    consonantsCounter = 0
    for char in tekst:
        if(char in vowels):
            vowelsCounter += 1
        elif(char in consonants):
            consonantsCounter += 1
    charDict = {"vowels": vowelsCounter, "consonants": consonantsCounter}
    return charDict
print(count_vowels_consonants(tekst))
