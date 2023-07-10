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

#Tutaj przejmuje w funkcji od usera rot, wykonac decoding lub encoding(mam tekst lub zmienną),mam obiekt typu tekst i dodaje go do buffeera,


#To jest funkcja startująca program...odpalamy ją z pliku main metodę run zaimportuje plik main sluzacy do startu programu.
# Każda funkcjonalnosc do innego pliku ma iść
class Manager:
    def run(self):
        while True:
            ## CALA LOGIKA PROGRAMU. WYBIERANIE, EXECUTOWANIE METOD/FUNCKJI.

            pass






def main():

    test_002 = Manager()
    #print(f"decoding function {test_001.decoding_text()}")
    # print(f"coding_text{test_001.coding_text()}")
    # #test_001.create_list_object(True)
    #test_002.coding_text()
    test_002.decoding_text()
if __name__ == "__main__":
    main()
