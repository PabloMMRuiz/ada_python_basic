import random
def sequential_search(item, l:list)->bool:
    """Returns True if the item is in the list else False. Equivalent to 'in' operator"""

    pos = 0
    while pos < len(l):
        if l[pos] == item:
            return True #The implementation given in the book uses an extra variable to stop the search once found. We can also return the moment we find it
        else:
            pos +=1
    return False

def ordered_sequential_search(item, l:list)->bool:
    """Returns True if the item is in the list else False. Equivalent to 'in' operator. 
    l must be ordered, else false negatives will occur"""

    pos = 0
    while pos<len(l):
        if l[pos] == item:
            return True
        elif l[pos] > item:
            return False
        else:
            pos +=1
    #Can also do all this with an super loop


"""
Suppose you are doing a sequential search of the list [15, 18, 2, 19, 18, 0, 8, 14, 19, 14]. How
many comparisons would you need to do in order to find the key 18?
1. 5
2. 10
3. 4
4. 2

2

Suppose you are doing a sequential search of the ordered list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18].
How many comparisons would you need to do in order to find the key 13?
1. 10
2. 5
3. 7
4. 6

7 (there we would stop searching)

"""

#Binary search o biseccion para los amigos

def binary_search(item, l:list, a=0, b=None)->bool:
    """Returns True if the item is in the list else False. Equivalent to 'in' operator. 
    l must be ordered, else false negatives will occur"""

    if b==None:
        b = len(l)
        #For the first call we need a value for b
    if b-a == 0:
        return False

    midpoint =(b+a)//2
    if l[midpoint] == item:
        return True
    elif l[midpoint] > item:
        return binary_search(item, l, a, midpoint)
    else:
        return binary_search(item, l, midpoint+1, b)
    
test_list =  [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] 
print(binary_search(18, test_list))
print(binary_search(6,test_list))
#Implemented following the improvement on the book: using slicing makes this worse than linear
print(test_list[0:5])


"""
Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the
recursive binary search algorithm. Which group of numbers correctly shows the sequence of
comparisons used to find the key 8.
1. 11, 5, 6, 8
2. 12, 6, 11, 8
3. 3, 5, 6, 8
4. 18, 12, 6, 8

2: 12,6,11,8
Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the
recursive binary search algorithm. Which group of numbers correctly shows the sequence of
comparisons used to search for the key 16?
1. 11, 14, 17
2. 18, 17, 15
3. 14, 17, 15
4. 12, 17, 15

4:12,17,15
"""

"""
In a hash table of size 13 which index positions would the following two keys map to? 27, 130
1. 1, 10
2. 13, 0
3. 1, 0
4. 2, 3

3: 1,0

Suppose you are given the following set of keys to insert into a hash table that holds exactly 11
values: 113, 117, 97, 100, 114, 108, 116, 105, 99. Which of the following best demonstrates the
contents of the has table after all the keys have been inserted using linear probing?
1. 100, __, __, 113, 114, 105, 116, 117, 97, 108, 99
2. 99, 100, __, 113, 114, __, 116, 117, 105, 97, 108
3. 100, 113, 117, 97, 14, 108, 116, 105, 99, __, __
4. 117, 114, 108, 116, 105, 99, __, __, 97, 100, 113

2.
"""

def bubble_sort(l:list)->list:
    """Sort the list in ascending order in place. Also returns the sorted list"""
    """Efficiency: O(n^2). We do n-1 passes (worst case), and do n-1 comparisons on the first pass, n-2 on the second...
        So its basically the sum of the n-1 firsts integers, which is a quadratic function.
    """
    #This is actually short bubble, done ahead of time
    sorted = False
    for pass_n in range(len(l)-1, 0, -1):
        sorted = True
        for i in range(pass_n):
            if l[i] > l[i+1]:
                sorted = False #Slight change in the book's code to stop the algorithm if the list is already sorted
                l[i], l[i+1] = l[i+1], l[i]
        if sorted:
            break
    return l

print(bubble_sort([5,2,4,3,5]))

"""#Bit of a test
for i in range(200):
    l = [random.randint(1,2000) for x in range(50)]
    print(l)
    l_sorted = bubble_sort(l)
    print(l_sorted)
    l.sort()
    print(l)
    print(l == l_sorted)
    if l !=l_sorted: 
        print("mal")
        break
    print(f"#############################\n")"""


"""Self Check
Suppose you have the following list of numbers to sort: [19, 1, 9, 7, 3, 10, 13, 15, 8, 12] which
list represents the partially sorted list after three complete passes of bubble sort?
1. [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
2. [1, 3, 7, 9, 10, 8, 12, 13, 15, 19]
3. [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
4. [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]


2: each ith pass of a bubble sort sends the ith biggest item to its position
"""

def selection_sort(l:list)->list:
    """Sort the list in ascending order in place. Also returns the sorted list"""
    """Efficiency: O(n^2). We do n-1 passes (worst case), and do n-1 comparisons on the first pass, n-2 on the second...
        So its basically the sum of the n-1 firsts integers, which is a quadratic function. This differs from bubble sort in that it does not make 
        an assignment for every comparison. This *is* relevant to efficiency but is not seen on O-notation
    """

    sorted = False
    for pass_n in range(len(l)-1,0,-1):
        sorted = True
        pos_max = 0
        for i in range(pass_n+1): #If you've done bubble sort this '+1' might be confusing: think that bubble sort looks to the item ahead
            #This doesn't, so we need i to reach len(l)
            if l[i] > l[pos_max]:
                sorted = False
                pos_max = i
        l[pos_max], l[pass_n] = l[pass_n], l[pos_max]
        if sorted:
            break
    return l

"""print(selection_sort([1,2,4,5,3]))
#Bit of a test
for i in range(200):
    l = [random.randint(1,2000) for x in range(50)]
    print(l)
    l_sorted = selection_sort(l)
    print(l_sorted)
    l.sort()
    print(l)
    print(l == l_sorted)
    if l !=l_sorted: 
        print("mal")
        break
    print(f"#############################\n")
"""
"""
#Bubble vs selection:
import timeit
t1 = timeit.Timer("bubble_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import bubble_sort,random")
print(f"Bubble sort: {t1.timeit(1000)}ms")
t2 = timeit.Timer("selection_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import selection_sort,random")
print(f"Selectin sort: {t2.timeit(1000)}ms")
#As we can see, while both are quadratic algorithms, the number of assignments really makes a difference
"""

"""Self Check
Suppose you have the following list of numbers to sort: [11, 7, 12, 14, 19, 1, 6, 18, 8, 20] which
list represents the partially sorted list after three complete passes of selection sort?
1. [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
2. [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
3. [11, 7, 12, 13, 1, 6, 8, 18, 19, 20]
4. [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
"""