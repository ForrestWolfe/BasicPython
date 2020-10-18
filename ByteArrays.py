from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i
print(data)
for b in data:
    print(hex(b))

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i



try:
    F = open('testfile.bin', 'wb')
    # if you do read(5) for example 5 will be the maximum number of bytes to be read.
    data = bytearray(F.read(5))
    F.close()
    for b in data:
        print(hex(b), end=' ')


except IOError as e:
    print("I/O error occuried:", e)

