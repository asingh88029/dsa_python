def search(listInput,si,li,key):
    if si>li:
        return -1
    midIndex = (si+li)//2
    mid = listInput[midIndex]    
    if(mid == key):
        return midIndex
    elif(mid>key):
        return search(listInput,si,midIndex-1,key)
    else:
        return search(listInput,midIndex+1,li,key)

inputList = [int(x) for x in input().split()]
keyToFind = int(input())
print(search(inputList,0,len(inputList)-1,keyToFind))