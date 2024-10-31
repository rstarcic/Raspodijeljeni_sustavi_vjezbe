# 7. zadatak

lozinka = input("Unesite lozinku: ")

def provjera_lozinke():
    lozinka = input("Unesite lozinku: ")

    def has_digit_or_upper(lozinka):
        has_upper = any(char.isupper() for char in lozinka)
        has_digit = any(char.isdigit() for char in lozinka)
        return has_digit and has_upper

    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif "password" in lozinka or "lozinka" in lozinka:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
    elif not has_digit_or_upper(lozinka):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    else:
        print("Lozinka je jaka")