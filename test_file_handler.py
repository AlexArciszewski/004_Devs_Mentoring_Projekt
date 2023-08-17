import json
from file_handler import FileHandler
from buffer import Text, Buffer



class TestFileHandler:
    """ Test for filehandler class"""

    def test_write_to_a_file(self):
        test = [Text(text='bbb', status=True, rot_type='1')]
        data = {
            "json 002: ": test
        }


        with open('json_data.json', 'w') as outfile:
            json.dump(data, outfile)  # data zapisane w postaci klasa,metodastatyczna()-create_json
            print({test})



