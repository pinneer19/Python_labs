import base64
import builtins
import inspect
import math
from collections.abc import Iterable
from utilities import get_class
from constants import PRIMITIVE_TYPES, DEFAULT_COLLECTIONS, ITERATOR_TYPE, BYTES_TYPE, FUNCTION_TYPE, MODULE_TYPE, \
    CELL_TYPE, IGNORE_CODE, CODE_TYPE, IGNORE_TYPES, IGNORE_DUNDER, CLASS_TYPE, OBJECT_TYPE

from types import ModuleType, CellType, FunctionType, \
    MethodType, CodeType


class Converter:
    def convert(self, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, ModuleType):
            return self._convert_module(obj)
        elif isinstance(obj, CellType):
            return self._convert_cell(obj)
        elif isinstance(obj, bytes):
            return self._convert_bytes(obj)
        elif isinstance(obj, DEFAULT_COLLECTIONS):
            return self._convert_collection(obj)
        elif isinstance(obj, Iterable):  # test
            return self._convert_iterable(obj)
        elif isinstance(obj, (FunctionType, MethodType)):
            return self._convert_function(obj)
        elif inspect.isclass(obj):
            return self._convert_class(obj)
        elif isinstance(obj, CodeType):
            return self._convert_code(obj)
        elif isinstance(obj, object):
            return self._convert_object(obj)
        else:
            raise Exception('Given type is not supported')

    def deconvert(self, obj):
        pass

    def _convert_collection(self, obj):
        if isinstance(obj, dict):
            return {key: self.convert(value) for key, value in obj.items()}
        if isinstance(obj, list):
            return [self.convert(item) for item in obj]
        else:
            return {
                '__type__': type(obj).__name__,
                '__data__': [self.convert(item) for item in obj]
            }

    def _convert_bytes(self, obj):
        return {
            '__type__': BYTES_TYPE,
            '__data__': obj.hex()  # convert bytes to hex string
        }

    def _convert_iterable(self, obj):
        return {
            '__type__': ITERATOR_TYPE,
            '__data__': [self.convert(item) for item in obj]
        }

    def _convert_function(self, obj):
        class_name = get_class(obj)

        globs = dict()
        for key, value in obj.__globals__.items():
            # __globals__ get all accessible from function global variables
            # __code__ provides access to function bytecode, co_names is tuple containing the names used by the bytecode
            # co_name - function name
            if key in obj.__code__.co_names and key != obj.__code__.co_name and value is not class_name:
                globs[key] = self.convert(value)

        # “Cell” objects are used to implement variables referenced by multiple scopes.
        # __closure__ stores tuple of closures like a cell objects
        closure = tuple()
        if obj.__closure__ is not None:
            closure = tuple(cell for cell in obj.__closure__ if cell.cell_contents is not class_name)

        return {
            '__type__': FUNCTION_TYPE,
            '__data__': self.convert(
                dict(
                    code=obj.__code__,
                    globals=globals,
                    name=obj.__name__,
                    argdefs=obj.__defaults__,  # A tuple containing defaults for argument with def values
                    closure=closure,
                    dictionary=obj.__dict__  # Dictionary of function attributes
                )
            ),
            '__method__': isinstance(obj, MethodType)  # or inspect.ismethod(obj)
        }

    def _convert_class(self, obj):

        # getmembers: Return all the members of an object in a list of (name, value) pairs sorted by name.
        data = {
            attr: self.convert(value)
            for attr, value in inspect.getmembers(obj)
            if attr not in IGNORE_DUNDER and type(value) not in IGNORE_TYPES
        }

        # get list of base classes exclude object
        data["__bases__"] = [
            self.convert(base) for base in obj.__bases__ if base != object
        ]

        data["__name__"] = obj.__name__

        return {
            '__type__': CLASS_TYPE,
            '__data__': data
        }

    def _convert_module(self, obj):
        return {
            '__type__': MODULE_TYPE,
            '__data__': obj.__name__
        }

    def _convert_cell(self, obj):
        return {
            '__type__': CELL_TYPE,
            '__data__': self.convert(obj.cell_contents)
        }

    def _convert_code(self, obj):

        attrs = [attr for attr in dir(obj) if attr.startswith('co')]

        return {
            '__type__': CODE_TYPE,
            '__data__': {attr: self.convert(getattr(obj, attr)) for attr in attrs if
                         attr not in IGNORE_CODE}
        }

    def _convert_object(self, obj):
        data = {
            '__class__': self.convert(obj.__class__),
            'attrs': {
                attr: self.convert(value) for attr, value in inspect.getmembers(obj)
                if not attr.startswith('__') and not isinstance(value, FunctionType)
                   and not isinstance(value, MethodType)
            }
        }

        return {
            '__type__': OBJECT_TYPE,
            '__data__': data
        }
