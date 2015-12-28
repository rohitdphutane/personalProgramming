from math import sqrt; from itertools import count, islice

num = 600851475143

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

factList = []
for i in range(1,int(sqrt(num)-1)):
    if num%i == 0 and isPrime(i):
        factList.append(i)

print max(factList)
