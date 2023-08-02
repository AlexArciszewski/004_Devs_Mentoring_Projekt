# metoda przyjmuje obiekt z buffera i zapisdo pliku z managera do pliku........

# funkcja bedzie miała opcje zapisu do pliku buffera
# metoda przyjmie dane z buffera jako parametr funkcji, buffer tez bedzie wykonywany z managera z menu.
import json
from buffer import Buffer
# json.dump() -> SERIALIZUJE obiekt python jako JSON i zapisuje do pliku. Przyjmuje dwa argumenty data, file

# json.dumps() -> SERIALIZUJE obiekt python jako json i zwraca json jako string. Przyjmuje jeden argument data.



class FileHandler:

    @staticmethod


    def write_to_a_file(zlota_rybka):



        data = {
            "json 001: ": zlota_rybka
        }


        with open('json_data.json', 'w') as outfile:
            json.dump(data, outfile)  #data zapisane w postaci klasa,metodastatyczna()-create_json




