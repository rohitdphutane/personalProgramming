#https://projecteuler.net/problem=50
import math
limit=1000000
def is_prime(a):
    return all(a % i for i in xrange(2, a))

primeList=[]
for x in range(limit,1000,-1):
    if x%1000 == 0:
            print x
    if is_prime(x):        
        primeList.append(x)

primeList = primeList[::-1]
print primeList
print len(primeList)

maxLength = 0
for j in range(0, len(primeList)):
    for i in range(1, len(primeList)):
        sublist = primeList[j:i]
        sumOfSubList = sum(sublist)
        #print sumOfSubList
        
        if sumOfSubList > 0 and len(sublist) > 10 and sumOfSubList < limit and is_prime(sumOfSubList):
            if maxLength == 0:
                maxLength = len(sublist)
            if maxLength < len(sublist):
                maxLength = len(sublist)
                print str(sumOfSubList) +", len: "+str(len(sublist))
        
