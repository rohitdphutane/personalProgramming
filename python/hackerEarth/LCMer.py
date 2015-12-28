import itertools
numberOfInputs = int(raw_input())

def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   lcm = 1
   while(x > 0 and y > 0):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


for numInp in range(0,numberOfInputs):
   inputFromUser = raw_input()
   n = int(inputFromUser.split()[0])
   l = int(inputFromUser.split()[1])
   r = int(inputFromUser.split()[2])
   x = int(inputFromUser.split()[3])
   print "inputFromUser: "+inputFromUser
   print str(n)+" - "+str(l)+" - "+str(r)+" - "+str(x)
   resultCount = 0
   li = []
   for num in range(l,r+1):
      for num1 in range(num,r+1):
         for i in itertools.product([num,num1], repeat=n):
            permuted = ''.join(map(str, i))
            #print "permuted:- "+permuted
            if permuted not in li and permuted[::-1] not in li:
               li.append(permuted)
               
   #li = list(set(li))
   print (li)
   resultCount = 0
   for numStr in range(0,len(li)):
      print "numStr: "+li[numStr]
      lcmValue = 1
      for indiNum in range(0,len(li[numStr])):
         #print "indiNum:- "+li[numStr][indiNum]  
         if indiNum + 1 < len(li[numStr]):
            lcmValue = lcm(int(li[numStr][indiNum]),int(li[numStr][indiNum+1]))
            #print li[numStr][indiNum]+" - "+li[numStr][indiNum+1]
         if lcmValue%x == 0:            
            print "lcmValue of "+li[numStr]+" is :- "+str(lcmValue)
            resultCount = resultCount + 1
            break

   print "resultCount:- "+str(resultCount)
       

print "Done"
   
