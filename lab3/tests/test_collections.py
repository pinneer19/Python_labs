import unittest

from serializer.serializers.json_serializer import JsonSerializer
from serializer.serializers.xml_serializer import XmlSerializer


class TestCollections(unittest.TestCase):
    def test_empty_list_json(self):
        value = []
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_empty_tuple_json(self):
        value = ()
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_empty_dict_json(self):
        value = {}
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_empty_set_json(self):
        value = set()
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_empty_list_xml(self):
        value = []
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_empty_tuple_xml(self):
        value = ()
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_empty_dict_xml(self):
        value = {}
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_empty_set_xml(self):
        value = set()
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_list_json(self):
        value = [None, 'sample', 34.0023442, True, 'sample2', False]
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_tuple_json(self):
        value = (None, 'sample', 34.0023442, True, 'sample2', False)
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_dict_json(self):
        value = {'key1': 'value1', 2: True, '???': None}
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_set_json(self):
        value = {None, 'sample', 34.0023442, True, 'sample2', False}
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_list_xml(self):
        value = [None, 'sample', 34.0023442, True, 'sample2', False]
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_tuple_xml(self):
        value = (None, 'sample', 34.0023442, True, 'sample2', False)
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_dict_xml(self):
        value = {'key1': 'value1', 2: True, '???': None}
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_simple_set_xml(self):
        value = {None, 'sample', 34.0023442, True, 'sample2', False}
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_complex_json(self):
        value = [None, {'key1': 'value1', 2: True, '???': None},
                 {None, 'sample', 34.0023442, True, 'sample2', False},
                 [{'key': ['value1', 'value2']}, (None, 'sample', 34.0023442, True, 'sample2', False)]]
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_complex_xml(self):
        value = [None, {'key1': 'value1', 2: True, '???': None},
                 {None, 'sample', 34.0023442, True, 'sample2', False},
                 [{'key': ['value1', 'value2']}, (None, 'sample', 34.0023442, True, 'sample2', False)]]
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)


if __name__ == '__main__':
    unittest.main()
