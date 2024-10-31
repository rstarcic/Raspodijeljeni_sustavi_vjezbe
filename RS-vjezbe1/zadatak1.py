# 1. zadatak - kalkulator
a = float(input("Unesi prvi broj: "))
b = float(input("Unesi drugi broj: "))
op = input("Unesi operator: ")

dozvoljeni_operator =("+", "-", "/", "*")
if op not in dozvoljeni_operator:
    print("Greška! Pogrešan operator")
else:
    if (op == "+"):
        print(f"Rezultat operacije {a} + {b} iznosi {a + b}")
    elif(op == "-"):
        print(f"Rezultat operacije {a} - {b} iznosi {a - b}")
    elif(op == "/"):
        if (b == 0):
            print("Dijeljenje ss nulo nije dopušteno")
        else: 
            print(f"Rezultat operacije {a} / {b} iznosi {a / b}")
    elif(op == "*"):
        print(f"Rezultat operacije {a} * {b} iznosi {a * b}")
