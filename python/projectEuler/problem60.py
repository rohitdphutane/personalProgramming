from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

primeList = []
for i in range(2, 30000):
    if isPrime(i):
        primeList.append(i)

#print primeList

possibleCandidates=[]
for prime1 in range(0,len(primeList)):
    for prime2 in range(prime1,len(primeList)):
        #print "prime1: "+str(primeList[prime1]) + ", prime2: "+str(primeList[prime2])
        oneTwo = int(str(primeList[prime1])+str(primeList[prime2]))        
        twoOne = int(str(primeList[prime2])+str(primeList[prime1]))        
        if not isPrime(oneTwo):
            continue
        if not isPrime(twoOne):
            continue       
        for prime3 in range(prime2,len(primeList)):
            oneThree = int(str(primeList[prime1])+str(primeList[prime3]))
            twoThree = int(str(primeList[prime2])+str(primeList[prime3]))
            threeOne = int(str(primeList[prime3])+str(primeList[prime1]))
            threeTwo = int(str(primeList[prime3])+str(primeList[prime2]))
            if not isPrime(twoThree):
                continue            
            if not isPrime(threeTwo):
                continue
            if not isPrime(oneThree):
                continue
            if not isPrime(threeOne):
                continue
            for prime4 in range(prime3,len(primeList)):
                oneFour = int(str(primeList[prime1])+str(primeList[prime4]))
                twoFour = int(str(primeList[prime2])+str(primeList[prime4]))
                threeFour = int(str(primeList[prime3])+str(primeList[prime4]))
                fourOne = int(str(primeList[prime4])+str(primeList[prime1]))
                fourTwo = int(str(primeList[prime4])+str(primeList[prime2]))
                fourThree = int(str(primeList[prime4])+str(primeList[prime3]))
                if not isPrime(oneFour):
                    continue
                if not isPrime(twoFour):
                    continue
                if not isPrime(threeFour):
                    continue
                if not isPrime(fourOne):
                    continue
                if not isPrime(fourTwo):
                    continue                
                if not isPrime(fourThree):
                    continue
                for prime5 in range(prime4,len(primeList)):
                    oneTwo = int(str(primeList[prime1])+str(primeList[prime2]))
                    oneThree = int(str(primeList[prime1])+str(primeList[prime3]))
                    oneFour = int(str(primeList[prime1])+str(primeList[prime4]))
                    oneFive = int(str(primeList[prime1])+str(primeList[prime5]))
                    twoOne = int(str(primeList[prime2])+str(primeList[prime1]))
                    twoThree = int(str(primeList[prime2])+str(primeList[prime3]))
                    twoFour = int(str(primeList[prime2])+str(primeList[prime4]))
                    twoFive = int(str(primeList[prime2])+str(primeList[prime5]))                    
                    threeOne = int(str(primeList[prime3])+str(primeList[prime1]))
                    threeTwo = int(str(primeList[prime3])+str(primeList[prime2]))
                    threeFour = int(str(primeList[prime3])+str(primeList[prime4]))
                    threeFive = int(str(primeList[prime3])+str(primeList[prime5]))
                    fourOne = int(str(primeList[prime4])+str(primeList[prime1]))
                    fourTwo = int(str(primeList[prime4])+str(primeList[prime2]))
                    fourThree = int(str(primeList[prime4])+str(primeList[prime3]))
                    fourFive = int(str(primeList[prime4])+str(primeList[prime5]))
                    fiveOne = int(str(primeList[prime5])+str(primeList[prime1]))
                    fiveTwo = int(str(primeList[prime5])+str(primeList[prime2]))
                    fiveThree = int(str(primeList[prime5])+str(primeList[prime3]))
                    fiveFour = int(str(primeList[prime5])+str(primeList[prime4]))
                    if not isPrime(oneFive):
                        continue
                    if not isPrime(twoFive):
                        continue
                    if not isPrime(fiveFour):
                        continue 
                    if not isPrime(threeFive):
                        continue
                    if not isPrime(fourFive):
                        continue
                    if not isPrime(fiveOne):
                        continue
                    if not isPrime(fiveTwo):
                        continue
                    if not isPrime(fiveThree):
                        continue
                    if not isPrime(fiveFour):
                        continue 
                    if isPrime(oneTwo) and isPrime(oneThree) and isPrime(oneFour) and isPrime(oneFive) and isPrime(twoOne) and isPrime(twoThree) and isPrime(twoFour) and isPrime(twoFive):
                        if isPrime(threeOne) and isPrime(threeTwo) and isPrime(threeFour) and isPrime(threeFive):
                            if isPrime(fourOne) and isPrime(fourTwo) and isPrime(fourThree) and isPrime(fourFive):
                                if isPrime(fiveOne) and isPrime(fiveTwo) and isPrime(fiveThree) and isPrime(fiveFour):
                                    print str(primeList[prime1])+" - "+str(primeList[prime2])+" - "+str(primeList[prime3])+" - "+str(primeList[prime4])+" - "+str(primeList[prime5])
            
