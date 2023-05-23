import unittest

from serializer.serializers.json_serializer import JsonSerializer
from serializer.serializers.xml_serializer import XmlSerializer


class ClassWithDecorator:
    some_field = 1111

    def decorator_func(func):
        def wrapper(self):
            return f'wrapped {func(self)}'

        return wrapper

    @decorator_func
    def to_be_decorated(self):
        return f'to be decorated with field {self.some_field}'


class ClassWithStaticMethod:

    @staticmethod
    def get_data(data):
        return f'got data: {data}'


class ClassWithClassMethod:
    @classmethod
    def get_data(cls):
        return 'this is class method'


class FirstParent:
    some_field = 'sss'

    def __init__(self, data):
        self.some_field = data

    def some_method(self, value):
        return value


class SecondParent:
    another_field = 'sss'

    def __init__(self, data):
        self.another_field = data

    def another_method(self, value):
        return value


class Child(FirstParent, SecondParent):
    def join_fields(self):
        return "".join([self.some_field, self.another_field])


class TestClassesObjects(unittest.TestCase):

    def test_class_w_decorator_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(ClassWithDecorator)
        deser_class = serializer.loads(packed)
        deser_obj = deser_class()
        assert deser_obj.to_be_decorated() == ClassWithDecorator().to_be_decorated()

    def test_class_w_decorator_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(ClassWithDecorator)
        deser_class = serializer.loads(packed)
        deser_obj = deser_class()
        assert deser_obj.to_be_decorated() == ClassWithDecorator().to_be_decorated()

    def test_class_object_dynamic_field_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(ClassWithDecorator)
        deser_class = serializer.loads(packed)
        deser_obj = deser_class()
        true_obj = ClassWithDecorator()
        deser_obj.some_field = 'dsfdsfds'
        true_obj.some_field = 'dsfdsfds'
        assert deser_obj.to_be_decorated() == true_obj.to_be_decorated()

    def test_class_object_dynamic_field_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(ClassWithDecorator)
        deser_class = serializer.loads(packed)
        deser_obj = deser_class()
        true_obj = ClassWithDecorator()
        deser_obj.some_field = 'dsfdsfds'
        true_obj.some_field = 'dsfdsfds'
        assert deser_obj.to_be_decorated() == true_obj.to_be_decorated()

    def test_class_w_static_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(ClassWithStaticMethod)
        deser_class = serializer.loads(packed)
        data_sample = [1, 23.4, (True, None)]
        assert ClassWithStaticMethod.get_data(data_sample) == deser_class.get_data(data_sample)

    def test_class_w_static_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(ClassWithStaticMethod)
        deser_class = serializer.loads(packed)
        data_sample = [1, 23.4, (True, None)]
        assert ClassWithStaticMethod.get_data(data_sample) == deser_class.get_data(data_sample)

    def test_class_w_cmethod_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(ClassWithClassMethod)
        deser_class = serializer.loads(packed)
        assert ClassWithClassMethod.get_data() == deser_class.get_data()

    def test_class_w_cmethod_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(ClassWithClassMethod)
        deser_class = serializer.loads(packed)
        assert ClassWithClassMethod.get_data() == deser_class.get_data()

    def test_class_inheritance_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(Child)
        deser_class = serializer.loads(packed)
        deser_obj = deser_class('weeee')
        true_obj = Child('weeee')
        assert true_obj.join_fields() == deser_obj.join_fields()

    def test_class_inheritance_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(Child)
        deser_class = serializer.loads(packed)
        deser_obj = deser_class('weeee')
        true_obj = Child('weeee')
        assert true_obj.join_fields() == deser_obj.join_fields()

    def test_class_mro_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(Child)
        deser_class = serializer.loads(packed)
        assert str(Child.__mro__) == str(deser_class.__mro__)

    def test_class_mro_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(Child)
        deser_class = serializer.loads(packed)
        assert str(Child.__mro__) == str(deser_class.__mro__)


if __name__ == '__main__':
    unittest.main()
