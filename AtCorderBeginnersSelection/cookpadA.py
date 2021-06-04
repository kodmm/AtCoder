import sys
fileName, a, b = sys.argv
listA = list(a)
listB = list(b)

reListA = list(reversed(listA))
reListB = list(reversed(listB))
lengthWork = len(b) if len(a) > len(b) else len(a)


listResult = []

for i in range(lengthWork):
    
    if reListA[i] == reListB[i]:
        listResult.insert(0, reListA[i] )
    else:
        break

result = ''.join(listResult)
if result:
    print(result)