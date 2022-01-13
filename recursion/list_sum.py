# Method1
def list_sum1(inputList):
    length=len(inputList)
    if(length==0):
        return 0
    return inputList[0]+list_sum1(inputList[1:])

# Method2
def list_sum2(inputList):
    length=len(inputList)
    if(length==0):
        return 0
    return inputList[length-1]+list_sum2(inputList[-2::-1])

# Method3
def list_sum3(inputList):
    length=len(inputList)
    if(length==0):
        return 0
    if(length%2==0):
        return list_sum3(inputList[0:length//2])+list_sum3(inputList[length//2:])
    else:
        return list_sum3(inputList[0:length//2])+inputList[length//2]+list_sum3(inputList[length//2+1:])

list1 = list(range(100))
print("List is ",list1)
print(list_sum1(list1))
print(list_sum2(list1))
print(list_sum3(list1))