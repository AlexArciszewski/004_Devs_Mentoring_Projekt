"""

Buffer to lista, która istnieje podczas działania programu, Trzyma zaszyfrowane, odszyfrowane
    wczytane z pliku(to w file_handler, z niego zapisujemy do pliku.
"""


class Text:
    def __init__(self, word, is_coded, code):
        self.word = 'word'
        self.is_coded = is_coded
        self.code = code
class Buffer:
# Tu lista obiektów Tworze obiekt klasy Text i appenduję do buffera...z klasy text
    data: list = []
    @staticmethod
    def add(value) -> None:
        Buffer.data.append(value)
    @staticmethod
    def remove(idx: int):
        """Removes the element with the given idx from the buffer"""
        if len(Buffer.data) >= idx:
            di = Buffer.data[idx]
            del Buffer.data[idx]
            print(f"Object {di}removed")
        return Buffer.data
#Tu lista obiektów...z klasy text
# print(base_text)
# coded_text = Code("bcb", 1)
# print(coded_text.coding())
#if __name__ == '__main__':
# base_text = Code("bcb", 1)
# word = base_text.coding()
#print(type(word))
tt = Text('xyz', True, "1")
Buffer.add(tt)              #add metoda statyczna data atrybut klasy buffer.add
#print(type(Buffer.data))
# base_text =Code("aaa", 3)
# word = base_text.coding()
ss = Text('xyz', True, "3")
Buffer.add(ss)
# base_text =Code("ccc", 2)
# word = base_text.coding()
uu = Text('xyz', True, "2")
Buffer.add(uu)
# print(base_text)
# print(word)
#print(Buffer.data)
#print(Buffer.data.add())
# print(f"The result is {Buffer.data} ")
#print(Buffer.data.add())
print("list", Buffer.data)
# Buffer.data.remove(2)
Buffer.remove(2)
print("list", Buffer.data)




from cipher import Code
from dataclasses import dataclass, astuple, asdict


@dataclass
class Text:
    text: str
    status: bool
    rot_type: str
    #zapis dictów do pliku do Json sprawdzić jak sie to robi


# t = Text("bcb", True,"1")  #to chiałem wrzucić do
# print(t)
# print(asdict(t))


# print("Class Buffer")
class Buffer:
# Tu lista obiektów Tworze obiekt klasy Text i appenduję do buffera...z klasy text
    data: list[Text] = []


    @staticmethod
    def add(value: Text) -> None:
        Buffer.data.append(value)

    def remove_from_buffer(idx:int):
        """Removes the element with the given idx from the buffer"""

        if len(Buffer.data) >= idx:
            di = Buffer.data[idx]
            del Buffer.data[idx]

            print(f"Object {di}removed")
        return Buffer.data




#Tu lista obiektów...z klasy text


# print(base_text)
# coded_text = Code("bcb", 1)
# print(coded_text.coding())

#if __name__ == '__main__':
base_text = Code("bcb", 1)

word = base_text.coding()

tt = Text(word, True, "1")
Buffer.add(tt)              #add metoda statyczna data atrybut klasy buffer.add

base_text = Code("aaa", 3)
word = base_text.coding()
ss = Text(word, True, "3")
Buffer.add(ss)

base_text = Code("ccc", 2)
word = base_text.coding()
uu = Text(word, True, "2")
Buffer.add(uu)



print(base_text)
print(word)
#print(Buffer.data)
#print(Buffer.data.add())
# print(f"The result is {Buffer.data} ")
#print(Buffer.data.add())
print("Score", Buffer.data)

Buffer.remove_from_buffer(2)
print("list", Buffer.data)






