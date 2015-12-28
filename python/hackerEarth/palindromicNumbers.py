#https://www.hackerearth.com/problem/algorithm/palindromic-numbers-7/

def calculatePalindromes(startNum,endNum):
    palindromeCount = 0
    for x in range(int(startNum),int(endNum)):       
        if list(str(x)) == list(reversed(str(x))):            
            palindromeCount = palindromeCount + 1            
        
    print(palindromeCount)
    
for inp in range(int(input())):
    inpStr = input().split()
    calculatePalindromes(inpStr[0],inpStr[1])
    
