import os
from stack import Stack

def par_checker(symbol_string:str)->bool:
    s = Stack()
    for c in symbol_string:
        if c == "(":
            s.push(c)
        elif c == ")":
            try:
                s.pop()
            except:
                return False
    if s.is_empty():
        return True
    else:
        return False
print(par_checker("(()()(()()))"))


def match_par_checker(symbol_string:str)->bool:
    #Works for (), [], {}
    s = Stack()
    index = 0
    for c in symbol_string:
        if c in "([{":
            s.push(c)
        elif c in ")]}":
            try:
                if matches(s.pop(), c): 
                    continue 
                else: 
                    return (False, index)
            except:
                return (False, index)
        index +=1
    if s.is_empty():
        return (True, 0)
    else:
        return (False, index)
    
def matches(open:str, close:str)->bool:
    #Auxiliar function for match_par_checkers
    openers = "([{"
    closers = ")]}"
    return openers.index(open) == closers.index(close)

print(match_par_checker("(fs([as][])){()[[()()()]]}"))
print(match_par_checker("((sv[]fa)d{a[])"))
print(match_par_checker("(()()(()()))))"))


def decimal_to_binary(num_dec:int)->str:
    s = Stack()
    while num_dec > 0:
        s.push(num_dec%2) #Remainder goes to the stack
        num_dec = num_dec // 2 #THEN we divide the number
    res = ""
    while not s.is_empty(): #Now we put the remainders in reverse order. Think that the first remainder indicates whether the number was even:
        #it's the smallest power of two in the binary string, and so on.
        res+=str(s.pop())
    return res

print(decimal_to_binary(128))

def decimal_to_base(num_dec:int, base:int)->str:
    aux = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #We need this for bases greater than 10: we do not have enough digits
    s = Stack()
    while num_dec>0:
        temp = num_dec%base 
        s.push(aux[temp])
        num_dec=num_dec//base
    res = ""
    while not s.is_empty():
        res+=s.pop()
    return res

print(decimal_to_base(16*16+11+16, 16))


def infix_to_postfix(op_string:str)->str:
    if not match_par_checker(op_string)[0]:
        raise ArithmeticError(f"Unmatched parenthesis at position {match_par_checker(op_string)[1]}")
    op_stack = Stack()
    op_string = op_string.split(" ")
    res = []
    operators = "(+-*/^" #Another implementation uses a dictionary. It is faster, but negligibly so
    for elem in op_string:
        if elem == "(":
            op_stack.push(elem)
            continue
        elif elem == ")":
            while True:
                left_elem = op_stack.pop()
                if left_elem == "(":
                    break
                res.append(left_elem)
        elif elem in operators:
            while not op_stack.is_empty() and operators.index(op_stack.peek())>=operators.index(elem):
                res.append(op_stack.pop())
            op_stack.push(elem)
        else:
            for char in elem:
                if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and char not in "0123456789":
                    raise TypeError("Unknown character")
            res.append(elem)
    while not op_stack.is_empty():
        res.append(op_stack.pop())
    return " ".join(res)
#This is the Shunting Yard Algorithm (Dijkstra) and uses Reverse Polish Notation
#https://en.wikipedia.org/wiki/Shunting_yard_algorithm
print(infix_to_postfix("( ( A + B ) * ( C + D ) ) / ( E - F )"))
print(infix_to_postfix("( ( A + B ) * ( C + D ) ) / ( EE09 - F )"))

def postfix_evaluation(postfix_expr:str)->int:
    operands_stack = Stack()
    postfix_expr = postfix_expr.split(" ")
    for elem in postfix_expr:
        if elem in "+-*/^":
            try:
                second_op = float(operands_stack.pop())
                first_op = float(operands_stack.pop())
            except:
                raise TypeError("Unknown value for conversion")
            if elem == "+":
                operands_stack.push(first_op+second_op)
            elif elem == "-":
                operands_stack.push(first_op-second_op)
            elif elem == "*":
                operands_stack.push(first_op*second_op)
            elif elem == "/":
                if second_op == 0:
                    raise ZeroDivisionError()
                operands_stack.push(first_op/second_op)
            elif elem == "^":
                operands_stack.push(first_op**second_op)
        else: operands_stack.push(elem)
    return operands_stack.pop()

print((52+4)*(2-3)/(5-9))
print(postfix_evaluation(infix_to_postfix("( 52 + 4 ) * ( 2 - 3 ) / ( 5 - 8 - 1 )")))
print(postfix_evaluation("7 8 + 3 2 + /"))

#Self check page 81:
#Postfix 10 + 3 * 5/(16 − 4): 
print((infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )")))
print(postfix_evaluation(infix_to_postfix("5 * 3 ^ ( 4 - 2 )")))



def stack_operate(operand_1, operand_2, operator):
    if operator in "+-*/^":
            try: #Since this is designed to work with stacks, we need to invert elements at some point for substraction and multiplication
                second_op = float(operand_1)
                first_op = float(operand_2)
            except:
                raise TypeError("Unknown value for conversion")
            if operator == "+":
                return(first_op+second_op)
            elif operator == "-":
                return(first_op-second_op)
            elif operator == "*":
                return(first_op*second_op)
            elif operator == "/":
                if second_op == 0:
                    raise ZeroDivisionError()
                return(first_op/second_op)
            elif operator == "^":
                return(first_op**second_op)
    else:
        raise ValueError("Unknown operand")


def direct_infix_evaluator(op_string:str):
    if not match_par_checker(op_string)[0]:
        raise ArithmeticError(f"Unmatched parenthesis at position {match_par_checker(op_string)[1]}")
    operators_stack = Stack()
    operands_stack = Stack()
    op_string = op_string.split(" ")
    res = []
    operators = "(+-*/^" #Another implementation uses a dictionary. It is faster, but negligibly so
    for elem in op_string:
        if elem == "(":
            operators_stack.push(elem)
            continue
        elif elem == ")":
            while True:
                left_elem = operators_stack.pop()
                if left_elem == "(":
                    break
                operands_stack.push(stack_operate(operands_stack.pop(), operands_stack.pop(), left_elem))
        elif elem in operators:
            while not operators_stack.is_empty() and operators.index(operators_stack.peek())>=operators.index(elem):
                operands_stack.push(stack_operate(operands_stack.pop(), operands_stack.pop(), operators_stack.pop()))
            operators_stack.push(elem)
        else:
            for char in elem:
                if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and char not in "0123456789":
                    raise TypeError("Unknown character")
            operands_stack.push(elem)
    while not operators_stack.is_empty():
        operands_stack.push(stack_operate(operands_stack.pop(), operands_stack.pop(), operators_stack.pop()))
    return operands_stack.pop()
print("\n\nAAAAAA")
print(direct_infix_evaluator("( 52 + 4 ) * ( 2 - 3 ) / ( 5 - 8 - 1 )"))



def calculator():
    op_string = input("Insert operation string separated by spaces. ex: '1 * ( 2 - 3 ): ")
    try:
        print(direct_infix_evaluator(op_string))
    except:
        print("Error")
    calculator()

os.system('cls' if os.name == 'nt' else 'clear')
calculator()

