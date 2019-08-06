from abc import ABC

class Class_(ABC):

    @property
    @abstractmethod
    def base_stats(self):
        return self.__base_stats

    @base_stats.setter
    @abstractmethod
    def base_stats(self, base_stats):
        self.__base_stats = base_stats

    @property
    @abstractmethod
    def resource(self):
        return self.__resource

    @property

