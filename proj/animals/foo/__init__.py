import importlib


class Foo:
    def __init__(self):
        self._load_properties(["eggs", "ham"])

    def _load_properties(self, property_names):
        for name in property_names:
            property_module = importlib.import_module(f"proj.animals.foo.properties.{name}")
            self.__setattr__(name, property_module.get_property())
