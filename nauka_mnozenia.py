import random
import os
from time import sleep
import sys


def main():
    # pobranie danych od użytkownika
    print("-" * 50)
    print("Witaj w programie do nauki mnożenia!")
    print("-" * 50)

    print("")
    print("-" * 50)
    z = input("Podaj dolną granicę mnożenia (1 - 10): ")
    x = input("Podaj górną granicę mnożenia (1 - 10): ")
    il_powt = input("Ile tur chcesz zrobić (minimum 5): ")
    print("\n")

    

    # sprawdzanie poprawności
    try:
        dol_granica = int(z)
        if dol_granica <1 or dol_granica > 10:
            print("Niepoprawna wartość !!!")
            print("Sprubój jeszcze raz, uruchom ponownie program.")
            sleep(3)
            sys.exit("Wartość dol_granica jest zaduża lub zamała")
    except:
        print("Niepoprawna wartość !!!")
        print("Sprubój jeszcze raz, uruchom ponownie program.")
        sleep(3)
        sys.exit("Zła wartość dol_granica, prawdopodobnie user użył zamiast liczby litery!")

    try:
        zakres = int(x)
        if zakres < 1 or zakres > 10:
            print("Niepoprawna wartość !!!")
            print("Sprubój jeszcze raz, uruchom ponownie program.")
            sleep(3)
            sys.exit("Wartość zakres jest zaduża lub zamała")
    except:
        print("Niepoprawna wartość !!!")
        print("Sprubój jeszcze raz, uruchom ponownie program.")
        sleep(3)
        sys.exit("Zła wartość x, prawdopodobnie user użył zamiast liczby litery!")

    try:
        il_powt = int(il_powt)
        if il_powt < 5:
            print("Podałeś zbyt niską wartość")
            print("Sprubój jeszcze raz, uruchom ponownie program.")
            sleep(3)
            exit("Wartość il_powt jest mniejsza od limitu (5)!!!")
    except:
        print("Niepoprawna wartość !!!")
        print("Sprubój jeszcze raz, uruchom ponownie program.")
        sleep(3)
        sys.exit("Zła wartość il_powt, prawdopodobnie user użył zamiast liczby litery!")

    # statystyki
    tura = 0
    blad = 0
    poprawne = 0

    # Pętla generująca pytania i odczytująca odpowiedzi
    for i in range(il_powt):
        tura += 1
        os.system("cls" if os.name == "nt" else "clear")
        print("-" * 50)
        print("\n")
        print(" Tura: " + str(tura))
        print("-" * 50)
        print("\n")
        liczba_1 = random.randint(1, 101)
        liczba_2 = random.randint(dol_granica, zakres)
        wynik = liczba_1 * liczba_2

        liczba_1 = str(liczba_1)
        liczba_2 = str(liczba_2)
        wynik_usera = input("ile jest: " + liczba_1 + " * " + liczba_2 + " = ")

        # sprawdzanie poprawności odpowiedzi
        try:
            wynik_usera = int(wynik_usera)
        except:
            print("\n\n")
            print("Odpowiedź nieprawidłowa!!!, musisz używać tylko cyfr!!!")
            sleep(5)
            sys.exit("Zła odpowiedź usera!!!")

        print("\n")
        print("-" * 50)

        # sprawdzanie poprawności wyników
        if wynik_usera == wynik:
            poprawne += 1
            print("\n\n")
            print("-" * 50)
            print("BRAWO!!! Wynik poprawny!!! Zdobywasz 1 punkt")
            print("-" * 50)
            sleep(5)
        else:
            blad += 1
            print("\n\n")
            print("-" * 50)
            print("NIESTETY BŁĄD!!! Prawidłowy wynik to: " + str(wynik))
            print("-" * 50)
            sleep(5)

    # Wyświetlenie statystyk odpowiedzi
    os.system("cls" if os.name == "nt" else "clear")
    print("-" * 50)
    print(f"Liczba poprawnych odpowiedzi: {poprawne}")
    print("-" * 50)
    print(f"Liczba złych odpowiedzi: {blad}")
    print("-" * 50)
    print("\n\n")

    srednia = il_powt / 2
    srednia_2 = il_powt / 3

    print("*" * 80)
    if blad > srednia:
        print("Słabo, musisz jeszcze poćwiczyć!!!")
    elif poprawne > srednia_2:
        print(
            "Jest nieźle, to naprawde dobry wynik, ale mogłoby być lepiej, poćwicz jeszcze!!!"
        )
    elif blad == 0:
        print(
            "Pięknie, twoje obliczenia są bardzo dobre!!! Możesz pochwalić się rodzicom!!!"
        )

    print("*" * 80)
    sleep(10)


# uruchomienie programu
if __name__ == "__main__":
    main()
