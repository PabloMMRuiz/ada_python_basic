"""
Write two Python functions to find the minimum number in a list. The first function should
compare each number to every other number on the list. O(n^2). The second function should be
linear O(n)
"""
import time

def min_cuadratic(l:list)->int:
    #Didn't really know how to slow this down
    min = None
    for n in l:
        m = True
        for other in l:
            if n>other:
                m = False
        if m:
            min = n
    return min

def min_linear(l:list)->int:
    min = l[0]
    for n in l[1:]:
        if n<min:
            min = n
    return min

if __name__ == "__main__":
    l = list(range(10000))
    print("Cuadratic:")
    start = time.time()
    print(min_cuadratic(l))
    print(time.time()-start)
    print("Linear:")
    start = time.time()
    print(min_linear(l))
    print(time.time()-start)
