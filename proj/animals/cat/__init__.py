import importlib


class Cat:

    def __init__(self, number_of_front_legs=2, number_of_hind_legs=2):
        self.number_of_front_legs = number_of_front_legs
        self.number_of_hind_legs = number_of_hind_legs
        self.set_dummies()

    _property_names = ['clawnum']

    def set_dummies(self):
        for name in self._property_names:
            setattr(self, '_' + name, None)

    for name in _property_names:
        exec(f'from proj.animals.cat.properties import {name}')
