# metoda przyjmuje obiekt z buffera i zapisdo pliku z managera do pliku........

# funkcja bedzie miała opcje zapisu do pliku buffera
# metoda przyjmie dane z buffera jako parametr funkcji, buffer tez bedzie wykonywany z managera z menu.
import json
import buffer
from src.buffer import Buffer

# json.dump() -> SERIALIZUJE obiekt python jako JSON i zapisuje do pliku. Przyjmuje dwa argumenty data, file

# json.dumps() -> SERIALIZUJE obiekt python jako json i zwraca json jako string. Przyjmuje jeden argument data.
class FileHandler:


    @staticmethod
    def write_to_a_file(zlota_rybka):  # TODO zlota_rybka out
        """method used to write a list of object to a dict"""

        data = {"data: ": zlota_rybka}

        with open("json_data.json", "w") as outfile:
            json.dump(
                data, outfile
            )  # data zapisane w postaci klasa,metodastatyczna()-create_json
            print(zlota_rybka)

    # TODO load to buffer / load fiel

    def load_from_a_file(zlota_rybka):
        """method used for loading the data from the json file """

        try:
            f = open(json_data.json)
        except FileNotFoundError:
            print("No such a file or directory")
        else:
            #buffer.show_buffer()
            print(zlota_rybka)