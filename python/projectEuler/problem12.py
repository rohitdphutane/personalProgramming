triangleNumList = []
for i in range(5000,10000):
    triangeNum = 0
    for j in range(1,i):
        triangeNum = triangeNum + j
    #print triangeNum
    if triangeNum != 0:
        triangleNumList.append(triangeNum)


print len(triangleNumList)

def findDivisors1(triangleNum):
    divisors = []
    for i in range(1,triangleNum+1):
        if triangleNum%i == 0:
            divisors.append(i)
    return divisors

def findDivisors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for triangleNum in triangleNumList:
    divisors = findDivisors(triangleNum)
    if len(divisors) > 500:
        print str(triangleNum)+" - "+str(len(divisors))
        break
        #print divisors
        
