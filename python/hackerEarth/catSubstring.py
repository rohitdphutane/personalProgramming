#https://www.hackerearth.com/november-clash-15/algorithm/cats-substrings/
numberOfN=int(raw_input())
nList=[]
for n in range(numberOfN):
    nList.append(raw_input())

numberOfM=int(raw_input())
mList=[]
for m in range(numberOfM):
    mList.append(raw_input())

print nList
print "---------"
print mList

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

for nVal in nList:
    #nSubStrList.extend(get_all_substrings(nVal))
    for mVal in mList:
        print nVal+" - "+mVal
        nSubStrList = get_all_substrings(nVal)
        mSubStrList = get_all_substrings(mVal)
        for nSubStr in nSubStrList:
            if nSubStr in mSubStrList:
                print "Substing: "+nSubStr
        #print nSubStrList


#nSubStrList = set(nSubStrList)
#mSubStrList = set(mSubStrList)

    
