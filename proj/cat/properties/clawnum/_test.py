from proj.cat import Cat


def test():
    standard_cat = Cat()
    assert standard_cat.clawnum == 18

    special_cat = Cat(number_of_front_legs=2, number_of_hind_legs=1)
    assert special_cat.clawnum == 14
