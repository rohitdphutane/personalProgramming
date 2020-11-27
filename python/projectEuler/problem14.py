originalN = 1
count = 0
numChainDict = {}

def calculateCollatz(n):
    global originalN
    global count
    global numChainDict
    res = 1
    if(n%2 ==0):
        res=n/2
    else:
        res=(3 * n)+1
    #print(res)
    count = count + 1
    if(res != 1):
        calculateCollatz(res)
    else:
        #print('count:'+str(count))
        numChainDict[count]= originalN
        count = 0
        
        
for i in range(10000,1000000):
    originalN = i
    calculateCollatz(i)

#print(numChainDict)
maxNumber = max(numChainDict, key=int)
print(maxNumber)

print(numChainDict[maxNumber])
