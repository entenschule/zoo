class Cat:

    def __init__(self, number_of_front_legs=2, number_of_hind_legs=2):
        self.number_of_front_legs = number_of_front_legs
        self.number_of_hind_legs = number_of_hind_legs
        self.set_dummies()

    def set_dummies(self):
        property_names = ['clawnum']
        for name in property_names:
            setattr(self, '_' + name, None)

    from proj.animals.cat.properties import clawnum
