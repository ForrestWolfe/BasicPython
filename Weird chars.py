from random import randint


class WeirdChars:
    def __init__(self):
        self.chars = []
        self.c = ''
        self.count = 0

    def get_char(self):
        for num in range(100, 400):
            self.chars.append('chr(' + str(num) + ')')

    def weird(self, integer):
        self.count = 0
        while self.count != integer:
            x = (chr(randint(0, len(self.chars))))
            self.count += 1
            self.c += x
        print(str(self.c))


obj = WeirdChars()
obj.get_char()
obj.weird(410)

"""alpha = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '[', 'chr(92)', 'chr(93)', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
                 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '9', '%')"""