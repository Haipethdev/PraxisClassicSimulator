import errors

class Character:

    def __init__(self, **kwargs):
        self.__race = kwargs['race']
        self.__class_ = kwargs['class']
        self.__level = kwargs['level']
        self.__stats = kwargs['stats']

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, race):
        try:
            self.__race = race
        except 


