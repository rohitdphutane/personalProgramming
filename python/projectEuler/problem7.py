from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

primeList = []
idx = 0
for i in range(1,1000000):
    if isPrime(i):
        idx = idx + 1
        if idx == 10001:
            print str(idx) +" - "+ str(i)
            break
