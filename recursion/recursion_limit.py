import sys

# sys.getrecursionlimit() is used to know current depth of recursion
print("Bydefault depth: ",sys.getrecursionlimit())

# sys.setrecursionlimit() is used to increase depth of recursion
sys.setrecursionlimit(2000)

print("Increased depth: ",sys.getrecursionlimit())