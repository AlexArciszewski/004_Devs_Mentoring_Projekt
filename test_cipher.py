import string
import pytest
from cipher import Code


class TestCipher:
    """ Class used for cipher methods tests"""

    def test_len_letters_collection(self):
        """Test method if the all alphabet is taken into consideration for coding"""
        code = Code('Hello World!', 13)
        assert code.len_letters_collection() == 95

    def test_coding(self):
        """Test for coding method from cipher.py"""
        code = Code('bbb', 1)
        assert code.coding() == 'ccc'

    def test_decoding(self):
        """Test for decoding method from cipher.py"""
        code = Code('bbb', 1)
        assert code.decoding() == 'aaa'

    def test_alphabet(self):
        """ Test for alphabet method"""
        code = Code('bbb', 1)
        raw_s = r""" 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        assert code.alphabet() == raw_s



#
