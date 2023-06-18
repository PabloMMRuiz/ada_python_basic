class Deque:
    def __init__(self) -> None:
        self.items = []

    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0, item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def is_empty(self)->bool:
        return True if len(self.items) == 0 else False
    
    def size(self)->int:
        return len(self.items)
    
    def __len__(self)->int:
        return len(self.items)