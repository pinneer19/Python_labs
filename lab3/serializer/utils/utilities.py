import inspect


def get_class(method):  # Get base class for method
    cls = getattr(inspect.getmodule(method), method.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0], None)
    if isinstance(cls, type):
        return cls
