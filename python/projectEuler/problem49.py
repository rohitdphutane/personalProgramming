#https://projecteuler.net/problem=49
from collections import Counter

def is_anagram(a,b):
    if len(a) != len(b):
         return False
    return  Counter(a) == Counter(b)


def is_prime(a):
    return all(a % i for i in xrange(2, a))

primeList=[]
for x in range(1000,10000):
    if is_prime(x):
        primeList.append(x)
        
print primeList

gotResult = False
for i in range(0,len(primeList)):
    if gotResult:
        break
    for j in range(i+1,len(primeList)):
        if is_anagram(str(primeList[i]),str(primeList[j])):
            k = primeList[j] + (primeList[j]-primeList[i])
            print "i: "+str(primeList[i])+", j: "+str(primeList[j])+", k: "+str(k)
            if k < 10000 and is_prime(k) and is_anagram(str(primeList[i]),str(k)) and primeList[i]!= 1487:
                print "Result:- "+str(primeList[i])+str(primeList[j])+str(k)
                gotResult = True
                break
                
            
    

