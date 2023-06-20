#Renamed to avoid conflic with existing queue implementation
#TODO: redo with Linked List
from singly_linked_list import SinglyLinkedList

class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self)->bool:
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
    
class QueueLinkedList:
    def __init__(self) -> None:
        self.items = SinglyLinkedList()
    def is_empty(self)->bool:
        return True if len(self.items) == 0 else False
    def enqueue(self, item):
        #Add an item to the Queue
        self.items.append(item)
    def dequeue(self)->any:
        #Returns, with removal, the queue's top element
        return self.items.pop()
    def size(self)->int:
        return len(self.items)
    def __len__(self)->int:
        return len(self.items)
    #This implementation has O(1) efficiency for all operations. It might work counterintuitively on the inside: we append the new element
    #to the end of the list and pop from index 0: this is due to it using a singly linked list: popping from the head would be O(n)