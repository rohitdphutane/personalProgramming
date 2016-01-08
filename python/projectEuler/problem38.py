getOut = False
numberList = []
for i in range(1,10):
    numberList.append(i)

print numberList

def checkForValidity(resultSum):
    #print "resultSum2:- "+str(resultSum)
    resultSum=''.join(sorted(resultSum))
    #print "resultSum2:- "+str(resultSum)
    if str(resultSum) == '123456789':
        return True
    else:
        return False

resultList = []
for num in range(190,500000):
    resultSum = ""
    for mul in range(1,10):
        mulVal = num * mul
        resultSum = resultSum +""+ str(mulVal)
        if len(resultSum) > 9:
            break
        #if len(resultSum) == 9:
            #print "resultSum1:- "+resultSum
        if len(resultSum) == 9 and checkForValidity(resultSum):
            resultList.append(resultSum)
            print "final result:- "+resultSum


resultList = map(int, resultList)
print max(resultList)
