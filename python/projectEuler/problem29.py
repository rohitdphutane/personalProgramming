maxLimit=100
resultList=[]
for i in range(2,maxLimit+1):
    for j in range(2,maxLimit+1):
        print str(i)+" - "+str(j)
        resultList.append(i**j)

       
resultList = set(resultList)
#print resultList
print len(resultList)
