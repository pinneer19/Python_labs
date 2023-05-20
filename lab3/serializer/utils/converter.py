import base64
import builtins
import inspect
import math
from collections.abc import Iterable

from constants import PRIMITIVE_TYPES, DEFAULT_COLLECTIONS, ITERATOR_TYPE, BYTES_TYPE

from types import ModuleType, CellType, FunctionType, \
    MethodType, CodeType


class Converter:
    def convert(self, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, bytes):
            return self._convert_bytes(obj)
        elif isinstance(obj, DEFAULT_COLLECTIONS):
            return self._convert_collection(obj)
        elif isinstance(obj, Iterable):  # test
            return self._convert_iterable(obj)
        elif isinstance(obj, (FunctionType, MethodType)):
            return self._pack_function(obj)
        elif inspect.isclass(obj):
            return self._pack_class(obj)
        elif isinstance(obj, ModuleType):
            return self._pack_module(obj)
        ...

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

    def _pack_function(self, obj):
        pass

    def _pack_class(self, obj):
        pass

    def _pack_module(self, obj):
        pass

    def _pack_cell(self, obj):
        pass

    def _pack_object(self, obj):
        pass
