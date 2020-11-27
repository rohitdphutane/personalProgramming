from num2words import num2words
sum = 0
        
for i in range(1,1001):
    numberText = num2words(i)
    numberText = numberText.replace('-','').replace(' ','')
    sum = sum + len(numberText)
    #print(numberText)

print(sum)
