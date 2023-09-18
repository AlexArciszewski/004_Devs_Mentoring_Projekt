from src.buffer import Buffer, Text
from src.cipher import Code
import pytest


class TestBuffer:
    """Class used for tests methods in buffer.py"""

    def test_default_buffer_data_is_empty(self):
        """Test method to check if the buffer is empty"""

        buffer_obj = Buffer()
        assert buffer_obj.data == []

    def test_add_method_buffer(self):
        """Test method for adding data to buffer"""

        text = Text("aaa", True, "1")
        buffer_obj = Buffer()

        assert buffer_obj.data == []
        assert len(buffer_obj.data) == 0

        buffer_obj.add(text)

        assert buffer_obj.data == [text]
        assert len(buffer_obj.data) == 1

        text2 = Text("bbb", True, "1")
        buffer_obj.add(text2)
        assert buffer_obj.data == [text, text2]
        assert len(buffer_obj.data) == 2


    def test_remove_method_buffer(self):
        """Test method for removing data from buffer"""

        text3 = Text("olo", True, "1")
        text4 = Text("ala", True, "1")
        buffer_obj = Buffer()
        assert len(buffer_obj.data) == 0
        buffer_obj.add(text3)
        buffer_obj.add(text4)
        assert len(buffer_obj.data) == 2
        buffer_obj.data.remove(text3)

        assert buffer_obj.data == [text4]
        assert len(buffer_obj.data) == 1
