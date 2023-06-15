#Renamed to avoid conflic with existing queue implementation
#TODO: redo with Linked List
class Queue:
    def __init__(self) -> None:
        self.items = []

    def if_empty(self)->bool:
        return True if len(self.items) == 0 else False
    def enqueue(self, item):
        #Add an item to the Queue
        self.items.insert(0, item)
    def dequeue(self)->any:
        #Returns, with removal, the queue's top element
        return self.items.pop()
    def size(self)->int:
        return len(self.items)
    def __len__(self)->int:
        return len(self.items)