def isPrime(num):
    #for integer in range of 2 and 1 + a num ^0.5
    for i in range(2, int(1 + num ** 0.5)):
        # if the number has a remainder of zero it is not a prime number
        if num % i == 0:
            return False
    return True


#This is going to give the is prime function a range of numbers to to scan threw and find the prime numbers
print('enter a number to get all the prime numbers leading up to it')
num = int(input("find prime numbers up to : "))
for i in range(1, num):
    if isPrime(i +1):
        print(i + 1, end=" prime ")

