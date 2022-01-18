def remove_x(inputString):
    if len(inputString)==0:
        return ""
    smallStringOutput = remove_x(inputString[1:])
    if inputString[0]=="x":
        return ""+smallStringOutput
    else:
        return inputString[0]+smallStringOutput

stringForInput = str(input())
print(remove_x(stringForInput))
        