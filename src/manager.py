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
from buffer import Buffer, Text
from cipher import Code
from typing import Callable
from menu import Menu
from file_handler import FileHandler
import json
import buffer

# Tutaj wszystko importujemy to sie ma nazywac manager to jest głowny plik z funkcjami

# Tutaj przejmuje w funkcji od usera rot, wykonac decoding lub encoding(mam tekst lub zmienną),mam obiekt typu tekst i dodaje go do buffeera,


# To jest funkcja startująca program...odpalamy ją z pliku main metodę run zaimportuje plik main sluzacy do startu programu.
# Każda funkcjonalnosc do innego pliku ma iść


class Manager:
    def __init__(self):
        self.buffer = Buffer()
        self.options: dict[int, Callable] = {
            1: self.coding_text,
            2: self.decoding_text,
            3: self.save_data_to_file,
            # 4: self.load_from_a_file,
            5: self.buffer.show_buffer,
            6: self.buffer.exit_the_program,
        }

    def input_text(self) -> str:
        text = input("please write the text You want to code or decode: ")
        print(f" you chose {text} ")
        print(
            f"After giving {text} . Now use input_rot method to input rot of of the text you want to code"
        )
        return text

    def input_rot(self) -> int:
        rot_type = int(
            input(f"please write the rot_type You want to use on the text given: ")
        )
        print(f"You chose {rot_type}")
        print(f"After giving text the rot you got is: {rot_type}")
        return rot_type

    def coding_text(self):
        text = self.input_text()
        rot = self.input_rot()

        test_obj = Code(text, rot)
        text_coded = test_obj.coding()
        coded_obj = Text(text_coded, True, str(rot))
        self.buffer.add(coded_obj)
        print(f"The result is: {coded_obj}")

    def decoding_text(self):
        text2 = self.input_text()
        rot2 = self.input_rot()
        test_obj_decod = Code(text2, rot2)
        dec_text = test_obj_decod.decoding()
        dec_obj = Text(dec_text, True, str(rot2))
        self.buffer.add(dec_obj)
        print(f"The result of decoding the {text2} is: {dec_obj} and {self.buffer}")

    def save_data_to_file(self):
        list_of_dicts = self.buffer.data_to_list_of_dicts()
        FileHandler.write_to_a_file(zlota_rybka=list_of_dicts)

    # def decoding_text(self):  # czy to dodajemy do programu To ma niby tekst odkodowac ale chyba musi być jakaś lokalizacja pliku z zapisaem????
    #     """Uncoding text using rot, creating text object Text obj. and adds it to the buffer"""
    #     print("Code the text")
    #     pass

    def run(self):
        while True:
            Menu.show_menu_options()
            user_choice = int(input("Please chose an option: "))
            if user_choice in self.options:
                self.options.get(user_choice)()
            else:
                print("The chosen option is invalid")
