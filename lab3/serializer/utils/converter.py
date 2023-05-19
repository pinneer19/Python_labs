import base64
import builtins
import inspect
import math

from .constants import PRIMITIVE_TYPES

from types import ModuleType, CellType, FunctionType, \
    MethodType, CodeType


class Converter:
    def convert(self, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, (list, tuple, set, dict)):
            return self._pack_collection(obj)
        elif self.__is_iter(obj):
            return self._pack_iterable(obj)
        elif isinstance(obj, (FunctionType, MethodType)):
            return self._pack_function(obj)
        elif inspect.isclass(obj):
            return self._pack_class(obj)
        elif isinstance(obj, ModuleType):
            return self._pack_module(obj)
        ...

    def unpack(self, obj):
        pass

    def __is_iter(self, obj):
        return hasattr(obj, '__iter__') and hasattr(obj, '__next__')

    def _pack_collection(self, obj):
        pass

    def _pack_iterable(self, obj):
        pass

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
