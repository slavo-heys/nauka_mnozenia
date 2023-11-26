import random
import os
from time import sleep
import sys


class Program:
    def __init__(self):
        # %% Zmienne potrzebne do działania programu
        self.tura = 0
        self.powtorzenia = 0
        self.dolna_liczba = 0
        self.gorna_liczba = 0
        self.poprawna_odpowiedz = 0
        self.bledna_odpowiedz = 0
        self.komunikat = "Podałeś złą wartość!!! Musisz podać liczbę od 1 do 10"
        self.komunikat_1 = "Zła wartość pola zapytania!!!"
        self.list = []

        # uruchomienie programu
        self.zapytanie()
        self.obliczenia()
        self.statystyka()

# %% definicja czyszczenia konsoli
    def clear_mon(self):
        os.system("cls" if os.name == "nt" else "clear")

# %% definicja kontroli błędu
    def blad_sys(self, komunikat):
        sys.exit(komunikat)

# %% definicja inicjowania pytań
    def zapytanie(self):
        self.tura = input("Podaj ilość wykonywanych działań (minimum 5): ")
        # sprawdzanie zmiennej czy jest int i czy jest większa od 5
        try:
            self.tura = int(self.tura)
            if self.tura < 5:
                print("-" * 50)
                print("Podałeś za niską wartość!!! Zacznij jeszcze raz!!!")
                print("-" * 50)
                sleep(5)
                Program()
        except:
            print("-" * 50)
            print(self.komunikat)
            print("-" * 50)
            sleep(10)
            self.blad_sys(self.komunikat_1)

        self.dolna_liczba = input("Podaj dolną granicę mnożnika (1-10): ")
        # sprawdzanie zmiennej czy jest int i czy mieści się w zakresie 1-10
        try:
            self.dolna_liczba = int(self.dolna_liczba)
            if self.dolna_liczba < 1 or self.dolna_liczba > 10:
                print("-" * 50)
                print("Podałeś złą wartość!!! Zacznij jeszcze raz!!!")
                print("-" * 50)
                sleep(5)
                Program()
        except:
            print("-" * 50)
            print(self.komunikat)
            print("-" * 50)
            sleep(10)
            self.blad_sys(self.komunikat_1)

        self.gorna_liczba = input("Podaj górną liczbę mnożnika (1-10): ")
        # sprawdzanie zmiennej czy jest int i czy mieści się w zakresie 1-10
        try:
            self.gorna_liczba = int(self.gorna_liczba)
            if self.gorna_liczba < 1 or self.gorna_liczba > 10:
                print("-" * 50)
                print("Podałeś złą wartość!!! Zacznij jeszcze raz!!!")
                print("-" * 50)
                sleep(5)
                Program()
        except:
            print("-" * 50)
            print(self.komunikat)
            print("-" * 50)
            sleep(10)
            self.blad_sys(self.komunikat_1)

# %% definicja liczenia i aktualizacji statystyk
    def obliczenia(self):
        for i in range(self.tura):
            self.powtorzenia += 1
            # losowanie liczb
            self.liczba_1 = random.randint(1, 10)
            self.liczba_2 = random.randint(
                self.dolna_liczba, self.gorna_liczba)
            # wynik mnozenia
            self.wynik = self.liczba_1 * self.liczba_2

            self.clear_mon()
            print("-" * 50)
            print(
                f"Tura: {self.powtorzenia}    |    Błędy: {self.bledna_odpowiedz}   |   Poprawne: {self.poprawna_odpowiedz}")
            print("-" * 50)
            print("\n")
            self.wynik_usera = input(
                f"Ile jest: {self.liczba_2} * {self.liczba_1} = ")
            # formatowanie do listy
            self.format = (str(self.liczba_2) + " * " + str(self.liczba_1) + " = " +
                           str(self.wynik_usera) + " | Poprawna odpowiedź: " + str(self.wynik))
            # sprawdzenie poprawnosci wyniku
            try:
                self.wynik_usera = int(self.wynik_usera)
            except:
                print("\n")
                print("-" * 50)
                print("Podałeś złą wartość!!! Zacznij jeszcze raz!!!")
                print("-" * 50)
                sleep(5)
                Program()

            print("\n")
            print("-" * 50)
            if self.wynik_usera == self.wynik:
                self.poprawna_odpowiedz += 1
                print("BRAWO! Zdobywasz 1 punkt.")
                print("-" * 50)
                sleep(5)
            else:
                self.bledna_odpowiedz += 1
                print(f"BŁĄD!!! Poprawny wynik to: {self.wynik}")
                self.list.append(self.format)
                sleep(10)

            print("\n\n")
            print("-" * 50)

#%% definicja wyswietlenia statystyki
    def statystyka(self):
        self.clear_mon()
        print("-" * 100)
        print("Twój wynik")
        print("-" * 100)
        print(f"Zdobyłeś {self.poprawna_odpowiedz} punktów.")
        print("-" * 100)
        print(f"Poprawne odpowiedzi: {self.poprawna_odpowiedz}")
        print(f"Błędne odpowiedzi: {self.bledna_odpowiedz}")
        print("-" * 100)

        # wyświetlenie wszystkich działań z złymi odpowiedziami o ile istnieją
        if self.bledna_odpowiedz > 0:
            print("\n\n")
            self.zapytanie = input(
                " Czy chcesz wyświetlić błędne działania (t/n)?")
            if self.zapytanie == "t" or self.zapytanie == "T" or self.zapytanie == "tak" or self.zapytanie == "Tak":
                self.clear_mon()

                i = len(self.list)
                for j in range(i):
                    print("-" * 50)
                    print(self.list[j])
                    print("\n")

                # zapis do pliku
                self.linia = "\n".join(self.list)
                f = open("wyniki.txt", mode="w")
                f.write(self.linia)
                f.close()  
                # konczymy czy nie
                self.koniec()              
            else:
                self.koniec()
        else:
            self.koniec()

#%% koniec ?
    def koniec(self):
        self.koniec = input("Koniec (t/n)?")
        if self.koniec == "t" or self.koniec == "T" or self.koniec == "tak" or self.koniec == "Tak":
            self.clear_mon()
            sys.exit("Koniec programu")
        else:
            self.clear_mon()
            Program()

start = Program()
