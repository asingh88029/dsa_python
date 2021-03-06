# Method1: by copying the list every time for recursion call.
# def find_x(inputList,cp,key):
#     length = len(inputList)
#     if(length==0):
#         return -1
#     if(inputList[0]==key):
#         return cp
#     else:
#         return find_x(inputList[1:],cp+1,key)

# Method2: Not copying the list every time for recursion call.
# def find_x(inputList,si,key):
#     length = len(inputList)
#     if(si==length):
#         return -1
#     if(inputList[si]==key):
#         return si
#     else:
#         return find_x(inputList,si+1,key)

#Method3: by copying the list every time for recursion call without passing current position
def find_x(inputList,key):
    length = len(inputList)
    if(length==0):
        return -1
    if(inputList[0]==key):
        return 0
    smallerListOutput=find_x(inputList[1:],key)
    if(smallerListOutput==-1):
        return -1
    else:
        return 1 + smallerListOutput

    
length = int(input())
listInput = [int(x) for x in input().split()]
key = int(input())

print(find_x(listInput,key)) 