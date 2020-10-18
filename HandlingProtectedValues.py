# This is how you would retrieve a value and still protect it from modification

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

    def getsum(self):
        return self.__sum


class AddingStack(Stack):
    def __init(self):
        Stack.__init__(self)
        self.__sum = 0