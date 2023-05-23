import math
import unittest

from serializer.serializers.json_serializer import JsonSerializer
from serializer.serializers.xml_serializer import XmlSerializer


def no_arg_func():
    return 'hello'


def arg_n_kwarg_func(pos1, pos2, kwarg1=True, kwarg2=True):
    return pos1, pos2, kwarg1, kwarg2


def rec_func(value):
    return value + rec_func(value - 1) if value != 0 else 0


some_module_lambda = lambda x: math.sin(x)


def closure_and_module_func(value_to_closure: int):
    closured_value = value_to_closure

    def closured_func(another_value: int):
        return math.cos(closured_value + another_value)

    return closured_func


class Iter:
    def __init__(self):
        self.data = ['some', {'keys': 'and', None: 'values'}]
        self.iterator = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)


class TestFunctions(unittest.TestCase):

    def test_no_arg_func_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(no_arg_func)
        assert no_arg_func() == serializer.loads(packed)()

    def test_no_arg_func_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(no_arg_func)
        assert no_arg_func() == serializer.loads(packed)()

    def test_arg_n_kwarg_func_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(arg_n_kwarg_func)
        assert arg_n_kwarg_func('first', 'second', kwarg2=False, kwarg1=True) == serializer.loads(packed)('first',
                                                                                                          'second',
                                                                                                          kwarg2=False,
                                                                                                          kwarg1=True)

    def test_arg_n_kwarg_func_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(arg_n_kwarg_func)
        assert arg_n_kwarg_func('first', 'second', kwarg2=False, kwarg1=True) == serializer.loads(packed)('first',
                                                                                                          'second',
                                                                                                          kwarg2=False,
                                                                                                          kwarg1=True)

    def test_rec_func_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(rec_func)
        assert rec_func(5) == serializer.loads(packed)(5)

    def test_rec_func_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(rec_func)
        assert rec_func(5) == serializer.loads(packed)(5)

    def test_closure_and_module_func_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(closure_and_module_func(4))
        assert closure_and_module_func(4)(5) == serializer.loads(packed)(5)

    def test_closure_and_module_func_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(closure_and_module_func(4))
        assert closure_and_module_func(4)(5) == serializer.loads(packed)(5)

    def test_lambda_w_module_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(some_module_lambda)
        assert some_module_lambda(-1) == serializer.loads(packed)(-1)

    def test_lambda_w_module_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(some_module_lambda)
        assert some_module_lambda(-1) == serializer.loads(packed)(-1)

    def test_iter_json(self):
        serializer = JsonSerializer()
        packed = serializer.dumps(Iter())
        unpacked = serializer.loads(packed)
        assert next(unpacked) == Iter().data[0]

    def test_iter_xml(self):
        serializer = XmlSerializer()
        packed = serializer.dumps(Iter())
        unpacked = serializer.loads(packed)
        assert next(unpacked) == Iter().data[0]


if __name__ == '__main__':
    unittest.main()

