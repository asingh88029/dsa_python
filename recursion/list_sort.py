def list_sort(inputList):
    length = len(inputList)
    if (length==0 or length==1):
        return True
    if(inputList[0]<=inputList[1]):
        return list_sort(inputList[1:])
    else:
        return False
       
list1=[1,2,3,4,5,89,7,8]
print(list_sort(list1))