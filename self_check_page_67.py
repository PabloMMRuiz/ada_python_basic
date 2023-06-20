from stack import Stack
"""Given the following sequence of stack operations, what is the top item on the stack when the
sequence is complete?"""

m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
m.peek()
#'z'

"""m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
    m.pop()
    m.pop()"""
#Error: as the loop runs for the second time, it will attempt to remove two elements, thee being only one

#Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.
def rev_string(my_str:str)->str:
    s = Stack()
    for char in my_str:
        s.push(char)
    res = ""
    while not s.is_empty():
        res +=s.pop()
    return res

print(rev_string("uno dos tres"))
