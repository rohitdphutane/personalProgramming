file = open('D:\Personal_stuff\personalProgramming\python\projectEuler\problem22\p022_names.txt', 'r')
fileContent = file.read()

fileContent = fileContent.replace("\"", "")
names = fileContent.split(",")
#names = names.sort()
names = sorted(names)
#print names
#print len(names)

idx = 0
resultVal = 0
for name in names:
    inputVal = name.lower()
    #print inputVal
    idx = idx + 1
    output = []
    for character in inputVal:
        number = ord(character) - 96
        output.append(number)
    mul = idx * sum(output)
    #print inputVal +" - "+ str(idx) +" - "+ str(sum(output)) +" - "+ str(mul)
    #print output
    resultVal = resultVal + mul
    #if inputVal == 'colin':

print resultVal
        
