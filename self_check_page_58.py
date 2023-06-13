"""
Which of the above list operations is not O(1)?
1. list.pop(0)
2. list.pop()
3. list.append()
4. list[10]
5. all of the above are O(1)

list.pop(0) is O(n)
"""

"""
Which of the above dictionary operations is O(1)?
1. 'x' in my_dict
2. del my_dict['x']
3. my_dict['x'] == 10
4. my_dict['x'] = my_dict['x'] + 1
5. all of the above are O(1)

All are O(1)
"""


#Discussion questions:
n=1
for i in range(n):
    for j in range(n):
        k = 2 + 2
#O(n^2)

for i in range(n):
    k = 2 + 2
#O(n)

i = n
while i > 0:
    k = 2 + 2
    i = i // 2

#O(log(n))

for i in range(n):
    for j in range(n):
        for k in range(n):
            k = 2 + 2
#O(n^3)

for i in range(n):
    k = 2 + 2
for j in range(n):
    k = 2 + 2
for k in range(n):
    k = 2 + 2
#O(n)

#Devise an experiment to verify that the list index operator is 𝑂(1)
from timeit import Timer
import random
"""for n in range(1000, 100001, 1000):
    x = list(range(n))
    t1 = Timer("x[random.randint(0,n-1)]", "from __main__ import n, x, random")
    print(f"Lenght of list: {n}. Time for random index access: {round(t1.timeit(10000), 5)}")

#Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries

for n in range(1000, 100001, 1000):
    x = {e:None for e in range(n)}
    t1 = Timer("x[random.randint(0,n-1)]=1", "from __main__ import n, x, random")
    print(f"Lenght of keyset: {n}. Time for random index set: {round(t1.timeit(10000), 5)}")"""

#Devise an experiment that compares the performance of the del operator on lists and dictionaries
"""
for n in range(1000, 10001, 2000):
    x = list(range(n))
    t1 = Timer("x.remove(random.randint(0,n-1))\nx=list(range(n))", "from __main__ import n, x, random")
    print(f"Lenght of list: {n}. Time for random index deletion: {round(t1.timeit(10000), 5)}")
    #Heavy overhead!
for n in range(1000, 10001, 5000):
    x = {e:None for e in range(n)}
    t1 = Timer("x.__delitem__(random.randint(0,n-1))\nx = {e:None for e in range(n)}", "from __main__ import n, x, random")
    print(f"Lenght of keyset: {n}. Time for random index deletion: {round(t1.timeit(10000), 5)}")"""
    #This did not feel constant

#Given a list of numbers in random order write a linear time algorithm to find the 𝑘th
#smallest number in the list. Explain why your algorithm is linear

def k_smallest_integer(l:list, k:int)->int:
    aux = [0]*(max(l)+1)
    for e in l:
        aux[e]+=1
    cont = 0
    res = 0
    while cont<k:
        if(aux[res]==0):
            res+=1
            continue
        else:
            aux[res]-=1
        cont+=1
    return res

print(k_smallest_integer([0,0,0,1,1,1,3,2,7], 8))

#It runs n+k times. Its is linear because index set in lists is O(1). It uses a lot of extra memory


#Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛)). Guessing this "improvement" refers to memory

def k_smallest_integer_mem_saver(l:list, k:int)->int:
    l.sort()
    return l[k]
print(k_smallest_integer([0,0,0,1,1,1,3,2,7], 8))


t2 = Timer("k_smallest_integer(list(range(200)), 8)", "from __main__ import k_smallest_integer")
print(t2.timeit(100000)) #Although theoretically faster, accessing so much memory slows it down. Buy better RAM
t2 = Timer("k_smallest_integer_mem_saver(list(range(200)), 8)", "from __main__ import k_smallest_integer_mem_saver")
print(t2.timeit(100000))
