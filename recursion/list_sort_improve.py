def list_sort(inputList,si):
    if(si==len(inputList)-1 or si == len(inputList)):
        return True
    if(inputList[si]<=inputList[si+1]):
        return list_sort(inputList,si+1)
    else:
        return False


listInput = [int(x) for x in input().split()]
print("Input list is sorted" if list_sort(listInput,0) else "Input list is not sorted")