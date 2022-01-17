def find_in_list(num,inputList):
    if(len(inputList)==0):
        return False
    if(inputList[0]==num):
        return True
    return find_in_list(num,inputList[1:])

inputListLength = int(input())
inputList = [int(x) for x in input().split()]
numSearch = int(input())
print(find_in_list(numSearch,inputList))