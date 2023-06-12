"""
Given the following code fragment, what is its Big-O running time?
"""
n=6

test = 0
for i in range(n):
    for j in range(n):
        test = test + i * j

#n^2


test = 0
for i in range(n):
    test = test + 1
for j in range(n):
    test = test - 1

#n

i = n
while i > 0:
    k = 2 + 2
    i = i // 2

#log(n)