# 14. zadatak
# a) Napišite funkciju isPrime() koja prima cijeli broj i vraća True ako je broj prost, a False ako nije. Prost broj je prirodan broj veći do 1 koji je dijeljiv jedino sa 1 i samim sobom.
# b) Napišite funkciju primes_in_range() koja prima dva argumenta:  start i end i vraća listu svih prostih brojeva u tom rasponu.

# a)
num = int(input("Unesite broj: "))
def isPrime(num): 
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if(num % i == 0):
            return False
    return True
print(isPrime(num))

# b)
start = int(input("Unesite početni broj: "))
end = int(input("Unesite završni broj: "))

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if isPrime(num):
            primes.append(num)
    return primes

print(primes_in_range(start,end))