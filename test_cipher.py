#from ..... import ..... importujemy funkcje do testów metoda testujaca zaczyna sie od test_

#from cipher import Code
import pytest
import string


# #metoda z pliku cipher
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
#
#
# @pytest.mark.parametrize('collection', [""" 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]"""])
# def test_alphabet(collection):
#     assert alphabet(collection) == True
#
#
#
# def main():
#     alphabet1 = alphabet("""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]""")
#     print(alphabet1)
#
#
# if __name__ == "__main__":
#     main()

#test podejscie nr 2


#metoda z pliku cipher

def alphabet(self) -> str:
    """Creates a string of letters ,numbers and signs that will be used for coding and decoding"""
    collection = "".join(
        [" ", string.digits, string.ascii_letters, string.punctuation]
    )
    ascii = []
    for i in range(32, 127):
            # print(chr(i))
        ascii.append(chr(i))

    # print(ascii)
    asci__string = "".join(ascii)
        # print(asci__string)
    collection == asci__string
    return collection

def test_alphabet():
    assert alphabet(""" 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]""") ==True