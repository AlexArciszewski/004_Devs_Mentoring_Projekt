"""

Buffer czyli taka lista, która sobie istnieje podczas działania programu, Trzyma zaszyfrowane, odszyfrowane
    wczytane z pliku, z niego zapisujemy do pliku.

"""
import cipher
#from cipher import *
from cipher import coding, decoding
#from .cipher import coding, decoding
#import cipher as cr   #cr.nazwa metody

#from cipher import coding

def buffer():
    return text








buffer()

""" 

    def coding(self) -> str:
        #Converting text to coded_text by moving index of the letter to new index by a jump_key

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
        #Converting coded_text to text  by moving index of the letter from new to previous index by a jump_key

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
                if new_index < 0:
                    new_index += self.len_letters_collection()
                text += self.alphabet()[new_index]
                #print(type(self.alphabet()[new_index]))
        return text



"""






