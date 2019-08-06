import numpy as np

class Fight:

    __t_step = 0.01

    def __init__(self, **kwargs):
        self.__length = kwargs['length']
        try:
            self.__fight = kwargs['fight']
        except KeyError:
            self.__fight = __defaultfight(self.__length)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def fight(self):
        return self.__fight

    @fight.setter
    def fight(self, fight):
        self.__fight = fight

    def __defaultfight(self, length)
        t_0 = 0
        t_f = length
        fight = []
        target = Character()
        ts = np.linspace(t_0, t_f, __t_step)
        for t in ts:
            fight_t = (target, t)  
            fight.append(fight_t)
        self.__fight = fight
