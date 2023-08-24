from .work import work


@property
def whiskers(self):
    return self._whiskers


@whiskers.setter
def whiskers(self, val):
    self._whiskers = val


@whiskers.getter
def whiskers(self):

    if self._whiskers is not None:
        return self._whiskers

    result = work(self)

    self.whiskers = result
    return result
