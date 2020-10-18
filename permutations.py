from itertools import permutations
import time


perm = []
for x in range(7):
     perm.append(x)

x = permutations(perm)

print(len(list(x)))

