import string


class Code:
    """Class used for creating the coding text"""

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
            ascii.append(chr(i))

        asci__string = "".join(ascii)
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
                # print(type(self.alphabet()[new_index]))
        return coded_text  # Text(coded_text, True, self.jump_key)

    def decoding(self) -> str:
        """Converting coded_text to text  by moving index of the letter from new to previous index by a jump_key"""

        text = ""
        x = self.coding()
        for letter in x:
            letter = letter.lower()
            if letter == " ":
                pass
            index = self.alphabet().find(letter)
            if index == 0:
                text += letter
            else:
                new_index = index - self.jump_key

                if new_index == 0:
                    new_index += self.len_letters_collection()
                text += self.alphabet()[new_index - self.jump_key]  # adde self.jump_key
                # print(type(self.alphabet()[new_index]))
        # print(new_index)
        # print(self.jump_key)
        # print(index)
        # print(self.alphabet()[new_index - self.jump_key])
        return text  # # Text(text, False, self.jump_key)


code_001 = Code(text="bbb ccc ddd", jump_key=1)
#print(code_001.coding())
# # print(code_001.alphabet())      #tworzę alfabet nie wiem czy musi więc być on w konstruktorze.....
# # print(code_001.len_letters_collection()) #wyznaczam długośc alfabetu czyli ile elementów to potrzebne do przejscia jesli skok będzie np 100
#print(code_001.decoding())  # decokduje słowo ale glówne a nie zakodowane

#print(f"For testing...{code_001.alphabet()}")
