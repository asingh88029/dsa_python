def list_sum3(inputList):
    length=len(inputList)
    if(length==0):
        return 0
    if(length%2==0):
        return list_sum3(inputList[0:length//2])+list_sum3(inputList[length//2:])
    else:
        return list_sum3(inputList[0:length//2])+inputList[length//2]+list_sum3(inputList[length//2+1:])

listLen = int(input())
listItem = [int(x) for x in input().split()]
print(list_sum3(listItem))