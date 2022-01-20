def replace(stringInput):
    if len(stringInput)==0 or len(stringInput)==1:
        return stringInput
    if(stringInput[0]+stringInput[1]=="pi"):
        return "3.14"+replace(stringInput[2:])
    else:
        return stringInput[0]+replace(stringInput[1:])

stringToInput = str(input())
print(replace(stringToInput))