def fact(num):
  if(num==1):
    return 1
  if(num==0):
    return 1
  return num * fact(num-1)

n = int(input("Enter no to find factorial:"))

print(fact(n))
