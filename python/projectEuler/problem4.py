shouldStop = False

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

palinList = []
for i in range(990,1,-1):
    if shouldStop:
        break
    for j in range(999,1,-1):
        mul = i*j
        if is_palindrome(str(mul)):
            print mul
            palinList.append(mul)
            if len(palinList) == 100000:
                shouldStop = True
                break

#print palinList
print max(palinList)
