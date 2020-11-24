import time
start_time = time.time()

for i in range(2000, 3000000000, 2):
    gotTheNumber = True
    for j in range(1, 20):
        if i%j != 0:
            gotTheNumber = False
            break
    if gotTheNumber:
        print('Number:'+str(i))
        break

print("---Completed in %s seconds ---" % (time.time() - start_time))
            
            
