#https://projecteuler.net/problem=41
from itertools import permutations
from math import sqrt; from itertools import count, islice

n = 7
numList=[]
someStr = ''
for i in range(1,n+1):
    someStr = someStr + str(i)

print someStr

def permute2(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            for perm in permute2(s[:i] + s[i+1:]):
                res += [c + perm]

    return res

#perms = [''.join(p) for p in permutations(someStr)]
perms = permute2(someStr)
print len(perms)
numberList = []

numberList = [int(i) for i in perms]
print "numberList"

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

numberList = sorted(numberList, key=int, reverse=True)
#print numberList
for num in numberList:
    print str(num) +" - "+ str(isPrime(num))
    if isPrime(num):
        print "pandigital prime: "+str(num)
        break
#print "Max element in the list:- "+str(max(numberList))

