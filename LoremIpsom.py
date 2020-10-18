from random import randint


class Lorem:
    def __init__(self, length, letters_per_line):
        self.alpha = []
        x = 32
        # most of the US keyboard. symbols and uppercase/lowercase.
        while x != 122:
            x += 1
            self.alpha.append(chr(x))
        self.c = []
        self.l0r3m = ''
        self.count = 0
        self.get_char(length, letters_per_line)

    def get_char(self, integer, aoc):
        try:
            for num in range(0, len(self.alpha)):
                while len(self.c) != integer:
                    z = randint(0, num)
                    z = z - randint(1, 14)
                    self.c.append(self.alpha[z])
                    self.count += 1
                    if self.count >= aoc:
                        self.c.append(' \n ')
                        self.count = 0
            print(self.l0r3m.join(self.c))
        except IndexError:
            pass


if __name__ == "__main__":
    total_amountOf_chars = int(input('Enter in the amount of characters in total:\t'))
    letters_per_line = int(input('Enter in the amount of letters per line:\t'))
    Lorem(length=total_amountOf_chars, letters_per_line=letters_per_line)
