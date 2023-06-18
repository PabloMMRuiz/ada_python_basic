#Palindrome checker

from deque import Deque


def palindrome_checker(check_string:str)->bool:
    d = Deque()
    for char in check_string:
        d.add_front(char)
    
    while d.size()>1:
        if d.remove_rear() != d.remove_front():
            return False
        
    return True

print(palindrome_checker("maeeddeeam"))