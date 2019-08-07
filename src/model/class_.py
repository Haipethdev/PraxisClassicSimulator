from abc import ABC

class Class_(ABC):

    @property
    @abstractmethod
    def power(self):
        pass

    @property
    @abstractmethod
    def stats_per_level(self):
        pass

    @property
    @abstractmethod
    def weapon_proficiencies(self):
        pass

    @property
    @abstractmethod
    def armour_proficiencies(self):
        pass
