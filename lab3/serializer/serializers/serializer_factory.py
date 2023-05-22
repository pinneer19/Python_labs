from .serializer_interface import ISerializer

class SerializerFactory:

    @staticmethod
    def get_serializer(type):
        ...