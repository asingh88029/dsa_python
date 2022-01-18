# Method1: starting from the end of the list
# def find(inputList,key,si):
#     length = len(inputList)
#     if(si==length or si == -1):
#         return -1
#     if(inputList[si]==key):
#         return si
#     else:
#         return find(inputList,key,si-1)

# Method2: starting from the end of the list using si
# def find(inputList,key,si):
#     length = len(inputList)
#     if(si==length):
#         return -1
#     smallerListOutput = find(inputList,key,si+1)
#     if(smallerListOutput==-1):
#         if(inputList[si]==key):
#             return si
#         else:
#             return -1
#     else:
#         return smallerListOutput

# Method3: starting from the end of the list but not using si
def find(inputList,key):
    length = len(inputList)
    if(length==0):
        return -1
    smallerListOutput = find(inputList[1:],key)
    if(smallerListOutput==-1):
        if(inputList[0]==key):
            return 0
        else:
            return -1
    else:
        return 1+smallerListOutput


length = int(input())
listInput = [int(x) for x in input().split()]
key = int(input())

print(find(listInput,key))
