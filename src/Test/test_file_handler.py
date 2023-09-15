# from src.buffer import Buffer, Text
# from src.manager import Manager
# import src.file_handler
# import json
# class TestFileHandler:
#
#
#      testing_buffer = Buffer()
#      """ Test for filehandler class"""
#      text_zzz = Text("aaa", True, "1")
#      text_kkk = Text("bbb", True, "2")
#      testing_buffer.add(text_zzz)
#      testing_buffer.add(text_kkk)
#      #print(f"testing buffer {testing_buffer}")
#      testing_buffer.data_to_list_of_dicts()
#      test_handler = testing_buffer.data_to_list_of_dicts()
#      print(test_handler)
#      Manager.write_to_a_file(test_rybka=test_handler)
#
#      data = {
#           "json 001: ": test_rybka
#      }
#
#      with open('json_data.json', 'w') as outfile:
#           json.dump(data, outfile)  # data zapisane w postaci klasa,metodastatyczna()-create_json
#           print({test_rybka})
from src.buffer import Buffer, Text
from dataclasses import asdict


class Test_FileHandler:
    """Test for filehandler class-if obj will be created and joined to json"""

    def test_creating_obj_text_class(self):
        """Method will create an obj of the Text class"""

        text_zzz = Text("aaa", True, "1")
        text_kkk = Text("bbb", True, "2")

        buffer_obj = Buffer()
        buffer_obj.add(text_zzz)
        buffer_obj.add(text_kkk)

        assert len(buffer_obj.data) == 2

    def test_data_to_list_of_dicts(self):
        """Test of method that creates the list of an obj"""

        text_zzz = Text("aaa", True, "1")
        text_kkk = Text("bbb", True, "2")

        buffer_obj = Buffer()
        buffer_obj.add(text_zzz)
        buffer_obj.add(text_kkk)

        that_list = buffer_obj.data
        list_of_dicts = []
        for elements in that_list:
            asdict(elements)
            list_of_dicts.append(asdict(elements))
            print(list_of_dicts)

        assert list_of_dicts == [
            {"text": "aaa", "status": True, "rot_type": "1"},
            {"text": "bbb", "status": True, "rot_type": "2"},
        ]
        assert len(list_of_dicts) == 2

    def test_list_of_dicts_saved_to_file(self):
        """Test of the method that creates the file with the list of an obj's"""

        text_zzz = Text("aaa", True, "1")
        text_kkk = Text("bbb", True, "2")

        buffer_obj = Buffer()
        buffer_obj.add(text_zzz)
        buffer_obj.add(text_kkk)

        that_list = buffer_obj.data
        list_of_dicts = []
        for elements in that_list:
            asdict(elements)
            list_of_dicts.append(asdict(elements))
        #
        # #assert FileHandler.write_to_a_file(list_of_dicts) == {"json 001: ": [{"text": "aaa", "status": True, "rot_type": "1"}, {"text": "bbb", "status": True, "rot_type": "2"}]}

        list_of_dicts = [
            {"text": "aaa", "status": True, "rot_type": "1"},
            {"text": "bbb", "status": True, "rot_type": "2"},
        ]

        # assert  == {"json 001: ": [{"text": "aaa", "status": True, "rot_type": "1"}, {"text": "bbb", "status": True, "rot_type": "2"}]}
