print("Enter the n number:")
num = int(input())

def print_n_to_1(n):
    if(n==0):
        return
    print(n)
    print_n_to_1(n-1)
    return

print_n_to_1(num)