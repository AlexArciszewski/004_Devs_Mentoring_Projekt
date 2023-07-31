import string


class Code:
    def __init__(self, text: str, jump_key: int) -> None:
        self.text = text
        self.jump_key = jump_key

    def alphabet(self) -> str:
        """Creates a string of letters ,numbers and signs that will be used for coding and decoding"""
        collection = "".join(
            [" ", string.digits, string.ascii_letters, string.punctuation]
        )
        ascii = []
        for i in range(32, 127):
            # print(chr(i))
            ascii.append(chr(i))

        #print(ascii)
        asci__string = (''.join(ascii))
        #print(asci__string)
        collection == asci__string
        return collection

    def len_letters_collection(self) -> int:
        """Creating the int which is a number of chars in a str of letters from def alphabet.
        This string will be used to go round if the jump_key is higher than number of chars
        """

        len_collection = len(self.alphabet())
        return len_collection

    def coding(self) -> str:
        """Converting text to coded_text by moving index of the letter to new index by a jump_key"""

        coded_text = ""
        for letter in self.text:
            letter = letter.lower()
            if letter == " ":
                coded_text += letter
                continue

            index = self.alphabet().find(letter)
            if index == -1:
                coded_text += letter
            else:
                new_index = index + self.jump_key
                if new_index >= self.len_letters_collection():
                    new_index -= self.len_letters_collection()
                coded_text += self.alphabet()[new_index]
                print(type(self.alphabet()[new_index]))
        return coded_text


    def decoding(self) -> str:
        """Converting coded_text to text  by moving index of the letter from new to previous index by a jump_key"""

        text = ""
        x = self.coding()

        for letter in x:
            letter = letter.lower()
            if letter == " ":
                pass
                #x = x + letter
                #continue

            index = self.alphabet().find(letter)
            if index == 0:
                text += letter
            else:
                new_index = index - self.jump_key

                if new_index == 0:
                    new_index += self.len_letters_collection()
                text += self.alphabet()[new_index - self.jump_key]   #adde selfj.ump_key
                # print(type(self.alphabet()[new_index]))
        # print(new_index)
        # print(self.jump_key)
        # print(index)
        # print(self.alphabet()[new_index - self.jump_key])
        return text # # Text(text, False, self.jump_key)


#
# def main():
#     menu_actions = {
#         '1': {
#             'name': 'Code a text',
#             'submenu': {
#                 '1': encrypt_text
#                 '2': back_to_menu
#
#             }
#         }
#     }
#
if __name__ == "__main__":
    code_001 = Code(text="aaa bbb ccc", jump_key=1)
    print(code_001.coding())
    # print(code_001.alphabet())      #tworzę alfabet nie wiem czy musi więc być on w konstruktorze.....
    # print(code_001.len_letters_collection()) #wyznaczam długośc alfabetu czyli ile elementów to potrzebne do przejscia jesli skok będzie np 100
    print(code_001.decoding())  #decokduje słowo ale gówne a nie zakodowoane


""" 
1.	Zakoduj plik.
    1.1	aby utworzyć nowy plik wciśnij…
        1.1.1	podaj nazwę pliku…(program zapisuje nazwę w buffer)
        1.1.2	aby napisać test do zakodowania wciśnij……(tekst idzie do buffer)
        1.1.3	aby zapisać i zakodować plik wciśnij……
        1.1.4	aby usunąć stworzony plik wciśnij…
        1.1.5	aby wrócić do glównego menu wybierz
    1.2	aby otworzyć istniejący plik wybierz….
        1.2.1	aby edytować tekst do zakodowania wciśnij……(tekst idzie do buffer)
        1.2.2	aby zapisać zakodowany plik wciśnij……
        1.2.3	aby usunąć stworzony plik wciśnij…
        1.2.4	aby wrócić do głównego menu wybierz

2.	Odkoduj plik.
    2.1 wybierz plik (to samo co w 1.2)
    2.2 aby zapisać odkodowany plik
    2.2 aby wrócić do menu wybierz
 
3.	 Wyjście.
 
4.	

"""
#ride or die