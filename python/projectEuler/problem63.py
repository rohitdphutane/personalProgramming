resultCount = 0
for number in range(1,1000):
    #print number
    for power in range(1,500):
        powerVal = number**power
        if len(str(powerVal)) == power:
            resultCount = resultCount + 1
            #print str(powerVal)+" - "+str(number)+" ** "+str(power)

print resultCount
            
