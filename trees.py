#List of Lists storage method:

def binary_tree(r):
    """Returns a binary tree with r as it's root's payload in a nested list form"""
    return [r,[],[]]
#I use a different concept than that used in the book: I expect the child to be a tree, as given in the recursive definition
def insert_left_child(r,c):
    """Insert a tree as the left child of the given root node. If there is already a left child node,
    substitute the child's left node for it"""
    if r[1] !=[]:
        c[1] = r[1]
        r[1] = c
    else:
        r[1] = c

def insert_right_child(r,c):
    """Insert a tree as the right child of the given root node. If there is already a right child node,
    substitute the child's right node for it"""
    if r[2] !=[]:
        c[2] = r[2]
        r[2] = c
    else:
        r[2] = c

def get_root_val(r):
    return r[0]

def set_root_val(r, new_val):
    r[0] = new_val

def get_left_chid(r):
    return r[1]

def get_right_child(r):
    return r[2]


tester = binary_tree("Hola")
print(tester)
insert_left_child(tester, binary_tree("hijo_izq"))
print(tester)
insert_left_child(tester, binary_tree("nuevo_hijo_izq"))
print(tester)
insert_right_child(tester, binary_tree("right_childo"))
print(tester)


"""
Self Check
Given the following statements:
x = binary_tree('a')
insert_left(x,'b')
insert_right(x,'c')
insert_right(get_right_child(x), 'd')
insert_left(get_right_child(get_right_child(x)), 'e')
Which of the answers is the correct representation of the tree?
1. ['a', ['b', [], []], ['c', [], ['d', [], []]]]
2. ['a', ['c', [], ['d', ['e', [], []], []]], ['b', [], []]]
3. ['a', ['b', [], []], ['c', [], ['d', ['e', [], []], []]]]
4. ['a', ['b', [], ['d', ['e', [], []], []]], ['c', [], []]]

3
"""

self_check = binary_tree("a")
insert_left_child(self_check, binary_tree("b"))
insert_right_child(get_left_chid(self_check), binary_tree("d"))
insert_right_child(self_check, binary_tree("c"))
insert_left_child(get_right_child(self_check), binary_tree("e"))
insert_right_child(get_right_child(self_check), binary_tree("f"))

print(self_check)

from stack import Stack
from binary_tree import BinaryTree

def build_parse_tree(exp:str):
    item_list = exp.split()
    parent_stack = Stack() #Could also do a doubly linked graph...
    res_tree = BinaryTree("Start")
    parent_stack.push(res_tree)
    curr_root = res_tree
    #Because of our method for adding left childs, we are not really relying on operation priority: parenthesis are needed for every operation
    for e in item_list:
        if e == "(":
            curr_root.insert_left("")
            parent_stack.push(curr_root)
            curr_root = curr_root.get_left_child()
        elif e not in ["+", "-", "*", "/"]:
            curr_root.set_root_val(e)
            curr_root = parent_stack.pop()
        elif e in ["+", "-", "*", "/"]:
            curr_root.set_root_val(e)
            curr_root.insert_right("")
            parent_stack.push(curr_root)
            curr_root = curr_root.get_right_child()
        elif e == ")":
            curr_root = parent_stack.pop()
        else:
            raise ValueError("Unknown operator or operand")
        
pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print("A")
