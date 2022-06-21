

from func1 import func1_module
from func2 import func2_module

class Func3Module:
    def __init__(self) -> None:
        print(f"module (name: {__name__}) initialized")

    def get_random_greeting(self):
        name = func1_module.random_name()
        number = func2_module.random_number() 
        return "Hello, %s! Your today's lucky number is %d." % (name, number)

print("_module_ run.")