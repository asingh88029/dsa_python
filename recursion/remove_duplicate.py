def remove(stringInput):
    if len(stringInput)==0 or len(stringInput)==1:
        return stringInput
    if stringInput[0]==stringInput[1]:
        updatedString = stringInput[0]+stringInput[2:] 
        return remove(updatedString)
    else:
        return stringInput[0]+remove(stringInput[1:])
stringToInput = str(input())
print(remove(stringToInput))