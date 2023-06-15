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
    for c in symbol_string:
        if c in "([{":
            s.push(c)
        elif c in ")]}":
            try:
                if matches(s.pop(), c): 
                    continue 
                else: 
                    return False
            except:
                return False
    if s.is_empty():
        return True
    else:
        return False
    
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
    aux = "0123456789ABCDEF" #We need this for bases greater than 10: we do not have enough digits
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
    op_stack = Stack()
    op_string = op_string.replace(" ", "")
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
            res.append(elem)
    while not op_stack.is_empty():
        res.append(op_stack.pop())
    return "".join(res)
#This is the Shunting Yard Algorithm (Dijkstra) and uses Reverse Polish Notation
#https://en.wikipedia.org/wiki/Shunting_yard_algorithm
print(infix_to_postfix("((A+B)*(C+D))/(E-F)"))

def postfix_evaluation(postfix_expr:str)->int:
    operands_stack = Stack()
    for elem in postfix_expr:
        if elem in "+-*/":
            left_op = float(operands_stack.pop())
            right_op = float(operands_stack.pop())
            if elem == "+":
                operands_stack.push(right_op+left_op)
            elif elem == "-":
                operands_stack.push(right_op-left_op)
            elif elem == "*":
                operands_stack.push(right_op*left_op)
            elif elem == "/":
                operands_stack.push(right_op/left_op)
        else: operands_stack.push(elem)
    return operands_stack.pop()

print((5+4)*(2-3)/(5-9))
print((infix_to_postfix("(5+4)*(2-3)/(5-9)")))
print(postfix_evaluation("78+32+/"))

#Self check page 81:
#Postfix 10 + 3 * 5/(16 − 4): 
print((infix_to_postfix("10 + 3 * 5/(16 - 4)")))
print(infix_to_postfix("5 * 3^(4 - 2)"))