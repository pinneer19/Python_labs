import unittest

from serializer.serializers.json_serializer import JsonSerializer
from serializer.serializers.xml_serializer import XmlSerializer


class TestPrimitives(unittest.TestCase):
    def test_primitive_int_json(self):
        value = 3456324324324324324324324325465436375687980907656789
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        return self.assertEqual(value, serializer.loads(packed))

    def test_primitive_float_json(self):
        value = 3456324324324324324324324325.465436375687980907656789
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_primitive_str_json(self):
        value = "some simple test"
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_primitive_bool_json(self):
        serializer = JsonSerializer()
        packedTrue = serializer.dumps(True)
        packedFalse = serializer.dumps(False)
        assert True == serializer.loads(packedTrue)
        assert False == serializer.loads(packedFalse)

    def test_primitive_none_json(self):
        value = None
        serializer = JsonSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_primitive_int_xml(self):
        value = 3456324324324324324324324325465436375687980907656789
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_primitive_float_xml(self):
        value = 3456324324324324324324324325.465436375687980907656789
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_primitive_str_xml(self):
        value = "some simple test"
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)

    def test_primitive_bool_xml(self):
        serializer = XmlSerializer()
        packedTrue = serializer.dumps(True)
        packedFalse = serializer.dumps(False)
        assert True == serializer.loads(packedTrue)
        assert False == serializer.loads(packedFalse)

    def test_primitive_none_xml(self):
        value = None
        serializer = XmlSerializer()
        packed = serializer.dumps(value)
        assert value == serializer.loads(packed)


if __name__ == '__main__':
    unittest.main()
