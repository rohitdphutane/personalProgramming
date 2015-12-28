shouldStop = False
limit = 1000
for a in range(1,limit):
    if shouldStop:
        break
    for b in range(a+1,limit):
        if shouldStop:
            break
        for c in range(b+1, limit):
            if (a*a + b*b) == c*c and a+b+c == 1000:
                print str(a)+" - "+str(b)+" - "+str(c)+" ->"+str(a+b+c)
                print a*b*c
                shouldStop = True
        
