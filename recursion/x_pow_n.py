def x_pow_n(xValue,yValue):
    if(yValue==1):
        return xValue
    if(yValue==0):
        return 1
    return xValue * x_pow_n(xValue,yValue-1)

print("Enter the x and n value seperated by space in same line:")

x,n = map(int,input().split())

print(x_pow_n(x,n))
