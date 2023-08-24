from .work import work


@property
def {{name}}(self):
    return self._{{name}}


@{{name}}.setter
def {{name}}(self, val):
    self._{{name}} = val


@{{name}}.getter
def {{name}}(self):

    if self._{{name}} is not None:
        return self._{{name}}

    result = work(self)

    self.{{name}} = result
    return result
