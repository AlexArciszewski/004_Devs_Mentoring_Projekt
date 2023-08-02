"""

Buffer to lista, która istnieje podczas działania programu, Trzyma zaszyfrowane, odszyfrowane
    wczytane z pliku(to w file_handler, z niego zapisujemy do pliku.
"""
from cipher import Code
from dataclasses import dataclass, astuple, asdict
#from manager import Manager


@dataclass
class Text:
    text: str
    status: bool
    rot_type: str


class Buffer:
    def __init__(self):
        self.data: list[Text] = []

    def add(self, value: Text) -> None:
        self.data.append(value)

    def remove_from_buffer(self, idx: int):
        """Removes the element with the given idx from the buffer"""
        try:
            if len(Buffer.data) >= idx:
                di = self.data[idx]
                del self.data[idx]
                print(f"Object {di}removed")
                return self.data
            else:
                if len(self.data) < idx:
                    raise ValueError("There is no idx with that number")
        except NameError:
            print("idx must be an integer not a string")

    def show_buffer(self):
        print(self.data)

    def data_to_list_of_dicts(self):
        my_list = list[self.data]
        my_list2 = self.data
        print(f"{my_list} that's a list of lists of obj's and {my_list2} is a list of obj's")
        list_of_dicts = []
        for elements in my_list2:
            asdict(elements)
            list_of_dicts.append(asdict(elements))
            #print(list_of_dicts)
            return list_of_dicts





def main():
    buffer = Buffer()
    text_zzz = Text("aaa", True, "1")
    text_kkk = Text("bbb", True, "2")
    #asdict(text_zzz)
    buffer.add(text_zzz)
    buffer.add(text_kkk)
    #print(buffer)
    #buffer.show_buffer()
    buffer.data_to_list_of_dicts()



if __name__ == '__main__':
    main()

