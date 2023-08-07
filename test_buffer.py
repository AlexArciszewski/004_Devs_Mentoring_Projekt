from buffer import Buffer, Text
from cipher import Code

class TestBuffer:
    def test_len_letters_collection(self):
        code = Code('Hello World!', 13)
        assert code.len_letters_collection() == 95

    def test_default_buffer_data_is_empty(self):
        buffer_obj = Buffer()
        assert buffer_obj.data == []

    def test_add_method_buffer(self):
        TEXT = Text("aaa", True, "1")
        buffer_obj = Buffer()


        # TEXT OBJ
        assert buffer_obj.data == []
        assert len(buffer_obj.data) == 0

        buffer_obj.add(TEXT)

        assert buffer_obj.data == [TEXT]
        assert len(buffer_obj.data) == 1


        TEXT2 = Text("bbb", True, "1")
        buffer_obj.add(TEXT2)
        assert buffer_obj.data == [TEXT, TEXT2]
        assert len(buffer_obj.data) == 2