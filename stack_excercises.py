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
