from prisma import Prisma

class PrismaSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Prisma()
        return cls._instance

prisma = PrismaSingleton.get_instance()
