def replace(stringInput,a,b):
    if len(stringInput)==0:
        return ""
    smallerStringOutput = replace(stringInput[1:],a,b)
    if(stringInput[0]==a):
        return b + smallerStringOutput
    else:
        return stringInput[0]+smallerStringOutput
    
stringInput = str(input())
a = str(input())
b= str(input())

print(replace(stringInput,a,b)," -> ",stringInput)