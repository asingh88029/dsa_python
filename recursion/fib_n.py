def fib_n(n):
    if(n<1):
        print("Invalid occurance...")
        return
    if(n==1 or n==2):
        return 1
    return fib_n(n-1)+fib_n(n-2)

print("Enter the number n:")
num = int(input())
print(fib_n(num))

