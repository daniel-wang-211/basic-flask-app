from optparse import Option
from .base import *

T=TypeVar("T")

class P1(Generic[T]):

    def __init__(self) -> None:
        super().__init__()
        self._data = []

    def add(self, t: T):
        self._data.append(t)

    def get(self, ind=0) -> Optional[T]:
        if ind < len(self._data):
            return self._data[ind]
        return None

class TestGen:

    def test_add1(self):
        p1 = P1[int]()
        p1.add(1.1)