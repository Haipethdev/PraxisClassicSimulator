from abc import ABC

class Class_(ABC):
    
    @property
    @abstractmethod
    def sta_to_hp(self):
        return 10

    @property
    @abstractmethod
    def armour_per_agi(self):
        return 2

    @property
    @abstractmethod
    def mana_per_int(self):
        return 15

    @property
    @abstractmethod
    def power(self):
        pass
    
    @property
    @abstractmethod
    def base_hp_60(self):
        pass

    @property
    @abstractmethod
    def base_power_60(self):
        pass
    
    @property
    @abstractmethod
    def base_stats_60(self):
        pass

    @property
    @abstractmethod
    def base_dodge(self):
        pass

    @property
    @abstractmethod
    def dodge_per_agi(self):
        pass

    @property
    @abstractmethod
    def ap_per_str(self):
        pass

    @property
    @abstractmethod
    def rap_per_agi(self):
        pass

    @property
    @abstractmethod
    def crit_per_agi(self):
        pass

    @property
    @abstractmethod
    def hp5_per_spi(self):
        pass
  
    @property
    @abstractmethod
    def base_hp5(self):
        pass

    @property
    @abstractmethod
    def weapon_proficiencies(self):
        pass

    @property
    @abstractmethod
    def armour_proficiencies(self):
        pass
