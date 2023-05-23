import unittest

from serializer.serializers.json_serializer import JsonSerializer
from serializer.serializers.xml_serializer import XmlSerializer

some_global_var = 1111


def global_func():
    global some_global_var
    return f'glob: {some_global_var}'


def non_local_func_out():
    var = 1234567890

    def non_local_func_in():
        nonlocal var
        return var + 1

    return non_local_func_in


class TestClassesObjects(unittest.TestCase):

    def test_global_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(global_func)
        deser_func = serializer.loads(packed)
        some_global_var = 324324
        assert global_func() == deser_func()

    def test_global_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(global_func)
        deser_func = serializer.loads(packed)
        some_global_var = 324324
        assert global_func() == deser_func()

    def test_nonlocal_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(non_local_func_out)
        deser_func = serializer.loads(packed)

        assert non_local_func_out()() == deser_func()()

    def test_nonlocal_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(non_local_func_out)
        deser_func = serializer.loads(packed)

        assert non_local_func_out()() == deser_func()()


if __name__ == '__main__':
    unittest.main()
