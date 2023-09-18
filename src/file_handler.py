# metoda przyjmuje obiekt z buffera i zapisdo pliku z managera do pliku........
#git commit --no-verify -m"<tutaj wklej swo jcommit msg"
# funkcja bedzie miała opcje zapisu do pliku buffera
# metoda przyjmie dane z buffera jako parametr funkcji, buffer tez bedzie wykonywany z managera z menu.
import json
import os.path
from functools import reduce
import buffer
import manager
from src.buffer import Text

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

    # TODO load to buffer / load file

    @staticmethod
    def load_from_a_file(path: str, buffer: 'Buffer'):

        check_file = os.path.isfile(path)
        print(check_file)
        if check_file == True:
           with open(path) as json_file:
              data = json.load(json_file)
              # https://www.geeksforgeeks.org/python-get-values-of-particular-key-in-list-of-dictionaries/

              # data = {"json 001: ": [{"text": "aaa", "status": True, "rot_type": "1"},
              #                        {"text": "bbb", "status": True, "rot_type": "2"}]}

              # for key in data:
              #     print(key)

              # print(data[key])
              # zlota_rybka = data[key]
              # zlota_rybka = [{"text": "aaa", "status": True, "rot_type": "1"},
              #                {"text": "bbb", "status": True, "rot_type": "2"}]

              # object = zlota_rybka[0]
              # txt = Text(object['text'], object['status'], object['rot_type'])

              for object in data:
                  txt = Text(object['text'], object['status'], object['rot_type'])
                  buffer.add(txt)
              #
              # # list_of_dicts_from_file = buffer.data_to_list_of_dicts()
              # # FileHandler.write_to_a_file(zlota_rybka=list_of_dicts_from_file)
              # #
              # # #buffer.show_buffer
              #
              #
              #
              #
              #
              #
              #
              #
              # for element in zlota_rybka:
              #     print(element)  # {"text": "aaa", "status": true, "rot_type": "1"} {"text": "bbb", "status": true, "rot_type": "2"}
              #
              # res_text = [sub["text"] for sub in zlota_rybka]
              # res_status = [sub["status"] for sub in zlota_rybka]
              # res_rot_type = [sub["rot_type"] for sub in zlota_rybka]
              # print(res_text, res_status, res_rot_type)
              #
              # x = len(res_text)
              # print(x)
              #
              # number_of_object = len(res_text)
              #
              # # https://www.geeksforgeeks.org/python-concatenate-two-lists-element-wise/
              # all = []
              #
              # for element in res_text:
              #     all.append(element)
              # for element in res_status:
              #     all.append(element)
              # for element in res_rot_type:
              #     all.append(element)
              # print(all)
              #
              # number_of_object = len(res_text)
              # # 2
              #
              # res_string_status = str(res_status)
              # print(res_string_status)  # [True, True]
              # print(res_string_status.replace("T", "t"))
              # print(res_string_status.replace("T", "t").replace("[", "").replace("]", "").replace(",", ""))
              # res_string_status_mod = res_string_status.replace("T", "t").replace("[", "").replace("]", "").replace(",",
              #                                                                                                       "")
              # res_list_status = list(res_string_status_mod.split(" "))
              # print(f"{res_list_status} fast track")
              #
              # all = []
              #
              # for element in res_text:
              #     all.append(element)
              # for element in res_list_status:
              #     all.append(element)
              # for element in res_rot_type:
              #     all.append(element)
              #
              # for txt, status, rot_type in zip(res_text, res_list_status, res_rot_type):
              #     print(txt, status, rot_type)
              #
              # for text in zip(res_text, res_list_status, res_rot_type):
              #     print(text[0], text[1], text[2])
              #     txt, status, rot_type = text
              #
              # print(f"That's all{all}")
              # number_of_object = len(res_text)  # 2 0,2,4 wyraz
              #
              #
              #   #czy tak można tworzyć obiekt klasy Text?
              # objects_from_file = [Text(object['text'], object['status'], object['rot_type']) for i in range(number_of_object)]
              # print(objects_from_file)
              #
              #




