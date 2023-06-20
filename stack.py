class Stack:
    def __init__(self) -> None:
        self.items = []
    def push(self, item):
        """Add an element to the top of the stack"""
        self.items.append(item)
    def pop(self):
        """Returns the stack's top element, removing it"""
        return self.items.pop()
    def peek(self):
        """Returns the stack's top element"""
        return self.items[-1]
    def is_empty(self)->bool:
        return True if len(self.items)==0 else False
    def size(self)->int:
        return len(self.items)
    def __len__(self): #This is what len(x) uses
        return len(self.items)
    
    