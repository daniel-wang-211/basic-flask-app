
import random
from base_module import base_module
from typing import Optional


cnt = [1]

class Func2Module:
    def __init__(self) -> None:
        self._min_number:Optional[int] = None
        self._max_number:Optional[int] = None

        print(f"module (name: {__name__}) initialized")

    def random_number(self):
        print(f"method(name: random_number) called.")
        if self._min_number is None:
            self._min_number = base_module.config().get("min_number", 0)
        if self._max_number is None:
            self._max_number = base_module.config().get("max_number", 1000)
        return random.randrange(self._min_number, self._max_number)  # type: ignore




print(f"module {__name__} run.")