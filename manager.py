"""
Fasada przyjmuje polecenia do:Zapisz plik,odczytaj to File_Handler,zaszyfruj odszyfruj....
- FileHandler odczyt, zapis do pliku, user podaje nazwe, wyjatki, Gdy chce zapisać do tego samego pliku to
      append(dodanie do pliku), - Ja polecam JSON.
- Szyfrowanie i Odszyfrowywanie.
- Buffer czyli taka lista, która sobie istnieje podczas działania programu, Trzyma zaszyfrowane, odszyfrowane
    wczytane z pliku, z niego zapisujemy do pliku.
- Menu
- Manager -> Główny plik z funkcjami, ** facade **
- run/main.py
- Exit

"""

#Tutaj wszystko importujemy to sie ma nazywac manager to jest głowny plik z funkcjami


#To jest funkcja startująca program...odpalamy ją z pliku main metodę run zaimportuje plik main sluzacy do startu programu.
# Każda funkcjonalnosc do innego pliku ma iść
class Manager:
    def run(self):
        while True:
            ## CALA LOGIKA PROGRAMU. WYBIERANIE, EXECUTOWANIE METOD/FUNCKJI.

            pass



""" 

Kod asci przeskakiwanie. ASCII 33 126 cyfry znaki plus litery...jak znak jest 126 rot 13 to daje literę 46 bo przekroczy 
126 znak 127 to del i trzeba od poczatku liczyć

"""



