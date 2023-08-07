# #from ..... import ..... importujemy funkcje do testów metoda testujaca zaczyna sie od test_
#
# from cipher import Code
# import pytest
# import string
#
#
# #metoda z pliku cipher
# #
# def alphabet(self) -> str:
#      """Creates a string of letters ,numbers and signs that will be used for coding and decoding"""
#
#      collection = "".join(
#          [" ", string.digits, string.ascii_letters, string.punctuation]
#      )
#      ascii = []
#      for i in range(32, 127):
#              # print(chr(i))
#          ascii.append(chr(i))
#
#      # print(ascii)
#      asci__string = "".join(ascii)
#          # print(asci__string)
#      collection == asci__string
#      return collection
#
#
#
# @pytest.mark.parametrize('collection', [""" 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]"""])
# def test_alphabet(collection)->str:
#      assert Code.alphabet("""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]""") == """ 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]"""
#
#
#
# def main():
#     code_001 = Code(text="bbb ccc ddd", jump_key=1)
#     code_001.alphabet()
#     #print(code_001.alphabet())
#     my_test = code_001.alphabet()
#     print(my_test)
#
# if __name__ == "__main__":
#     main()

#test podejscie nr 2


#metoda z pliku cipher
#
# def alphabet(self) -> str:
#     """Creates a string of letters ,numbers and signs that will be used for coding and decoding"""
#     collection = "".join(
#         [" ", string.digits, string.ascii_letters, string.punctuation]
#     )
#     ascii = []
#     for i in range(32, 127):
#             # print(chr(i))
#         ascii.append(chr(i))
#
#     # print(ascii)
#     asci__string = "".join(ascii)
#         # print(asci__string)
#     collection == asci__string
#     return collection
#
# def test_alphabet():
#     assert alphabet(""" 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]""") ==True

import pytest
from manager import Manager

#jak zrobić taka metodę

    # def input_text(self) -> str:
    #     text = input("please write the text You want to code or decode: ")
    #     print(f" you chose {text} ")
    #     print(f"After giving {text} . Now use input_rot method to input rot of of the text you want to code")
    #     return text


from cipher import Code
from buffer import Buffer

class TestBuffer:
    def test_len_letters_collection(self):
        code = Code('Hello World!', 13)
        assert code.len_letters_collection() == 95
    

    def test_default_buffer_data_is_empty(self):
         buffer_obj = Buffer()
         assert buffer_obj.data == []

    def test_add_method_buffer(self):
        buffer_obj = Buffer()

        assert buffer_obj.data == []
        assert len(buffer_obj.data) == 0

        buffer_obj.add(TEXT)

        assert buffer_obj.data == [TEXT]
        assert len(buffer_obj.data) == 1