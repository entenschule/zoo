from .work import work


@property
def clawnum(self):
    return self._clawnum


@clawnum.setter
def clawnum(self, val):
    self._clawnum = val


@clawnum.getter
def clawnum(self):

    if self._clawnum is not None:
        return self._clawnum

    result = work(self)

    self.clawnum = result
    return result
