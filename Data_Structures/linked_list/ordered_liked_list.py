from node import Node
class OrderedList:
    """Objects with a comparison operation expected"""
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __len__(self)->int:
        return self.length
    
    
    def __contains__(self, item)->bool:
        curr_node = self.head
        while curr_node != None:
            if curr_node.get_data() == item:
                return True
            elif curr_node.get_data() > item:
                return False
            curr_node = curr_node.get_next()
        
        return False

    def __str__(self) -> str:
        res = str(self.head.get_data())
        curr_node = self.head.get_next()
        while curr_node != None:
            res = res +", "+ str(curr_node.get_data())
            curr_node = curr_node.get_next()
        return "["+res+"]"
    
    def __getitem__(self, index:int):
        if -self.length >=index or index>=self.length:
            raise IndexError("Index out of range")
        elif 0<=index: 
            pos = 0
            curr_node = self.head
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            return curr_node.get_data()
        else: 
            index = self.length + index #Index is negative here
            pos = 0
            curr_node = self.head
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            return curr_node.get_data()
        
    #It doesn't really make sense to have setitem here



    def is_empty(self)->bool:
        return self.head == None

    def add(self, item):
        prev_node = None
        curr_node = self.head
        while curr_node !=None:
            if curr_node.get_data()>item:
                break
            else:
                prev_node, curr_node = curr_node, curr_node.get_next()
        temp = Node(item)
        if prev_node == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(curr_node)
            prev_node.set_next(temp)
    
    def index(self, item)->int:
        pos = 0
        if self.is_empty():
            raise ValueError()
        else: 
            curr_node = self.head
        while curr_node.get_next() != None:
            if curr_node.get_data() == item:
                return pos
            elif curr_node.get_data() > item:
                raise ValueError()
            else:
                pos +=1
                curr_node = curr_node.get_next()
        raise ValueError()

    def pop(self, index=0)->any:
        if 0>index or index>=self.length:
            raise IndexError("Pop index out of range")
        elif index == 0:
            temp = self.head.get_data() #Store the value *before* changing head
            self.head = self.head.get_next()
            self.length -=1
            return temp
        #As our list is singly linked we can't traverse backwards. pop() will be O(n)
        else:
            pos = 1
            prev_node =self.head
            curr_node = self.head.get_next() if not self.is_empty() else None
            while curr_node.get_next() != None:
                if pos == index:
                    prev_node.set_next(curr_node.get_next())
                    self.length-=1
                    return curr_node.get_data()
                else:
                    pos+=1
                    prev_node =curr_node
                    curr_node = curr_node.get_next()