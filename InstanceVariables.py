class ExampleClass:
    def __init__(self, val=1):
        self.first = val

    def setSecond(self,  val= 2):
        self.second = val

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.Third = 5


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)

print('MAKING THE INSTANCE VARIABLES PRIVATE THIS IS THE EASIEST WAY TO CONCEAL YOUR CODE')

class Test:
    def __init__(self, val = 1):
        self.__first = val

    def SetSec(self, val = 2):
        self.__second = val

example1 = Test()
example2 = Test(2)

example2.SetSec(3)

example3 = Test(4)
example3.__third = 5


print(example1.__dict__)
print(example2.__dict__)
print(example3.__dict__)

