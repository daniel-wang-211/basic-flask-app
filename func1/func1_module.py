import random
from base_module import base_module

cnt = [1]

class Func1Module:
    def __init__(self, name:str = "default") -> None:
        self._name = name
        global cnt
        cnt[0] += 1
        self._cnt = cnt[0]
        print(f"module (name: {self._name}, cnt: {self._cnt}) initialized")

    def method(self):
        print(f"method(name: {self._name}, cnt: {self._cnt}) called.")

    def random_name(self):
        name_list = base_module.names()

        return random.choice(name_list)


print("_module_ run.")