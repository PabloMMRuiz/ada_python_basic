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
print(binary_search(8, test_list))
print(binary_search(42,test_list))
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

1: 1,10

Suppose you are given the following set of keys to insert into a hash table that holds exactly 11
values: 113, 117, 97, 100, 114, 108, 116, 105, 99. Which of the following best demonstrates the
contents of the has table after all the keys have been inserted using linear probing?
1. 100, __, __, 113, 114, 105, 116, 117, 97, 108, 99
2. 99, 100, __, 113, 114, __, 116, 117, 105, 97, 108
3. 100, 113, 117, 97, 14, 108, 116, 105, 99, __, __
4. 117, 114, 108, 116, 105, 99, __, __, 97, 100, 113

2.
"""

print(108%11)