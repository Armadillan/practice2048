import random

class Class:
    def __init__(self) -> None:
        pass

    @property
    def x(self):
        return random.randint(0, 1)

X = Class()
a = X.x
for i in range(10):
    
    print(a)