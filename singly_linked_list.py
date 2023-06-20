from node import Node
class SinglyLinkedList:
    def __init__(self) -> None:
        self.rear = None
        self.head = None
        self.length = 0 #So len operation is linear. Could be solved with traversing: small memory improvement at greater time cost
    def __len__(self)->int:
        return self.length

    def __contains__(self, item)->bool:
        curr_node = self.rear
        while curr_node != None:
            if curr_node.get_data() == item:
                return True
            curr_node = curr_node.get_next()
        
        return False

    def __str__(self) -> str:
        res = str(self.rear.get_data())
        curr_node = self.rear.get_next()
        while curr_node != None:
            res = res +", "+ str(curr_node.get_data())
            curr_node = curr_node.get_next()
        return "["+res+"]"
    
    def __getitem__(self, index:int):
        if -self.length >=index or index>=self.length:
            raise IndexError("Index out of range")
        elif 0<=index: 
            pos = 0
            curr_node = self.rear
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            return curr_node.get_data()
        else: 
            index = self.length + index #Index is negative here
            pos = 0
            curr_node = self.rear
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            return curr_node.get_data()
        
    def __setitem__(self, index, item):
        if -self.length >=index or index>=self.length:
            raise IndexError("Index out of range")
        elif 0<=index: 
            pos = 0
            curr_node = self.rear
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            curr_node.set_data(item)
        else: 
            index = self.length + index #Index is negative here
            pos = 0
            curr_node = self.rear
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            curr_node.set_data(item)

    def is_empty(self)->bool:
        return self.rear == None
# [1,2,3,4,5]: 1 is rear, 5 is head
    def add(self, item):
        """Pushes an item to the rear (index 0) of the list"""
        temp = Node(item)
        temp.set_next(self.rear)
        self.rear = temp
        if len(self)==0:
            self.head = temp
        self.length +=1

    def remove(self, item):
        prev_node =self.rear
        curr_node = self.rear.get_next() if not self.is_empty() else None
        if self.rear.get_data()==item:
            self.rear = self.rear.get_next()
        while curr_node != None:
            if curr_node.get_data() == item:
                prev_node.set_next(curr_node.get_next()) #We "skip" the current node and leave it out of the list.
                self.length -=1
                if(curr_node.get_next() == None): #In case we delete the head, we need to update it
                    self.head = prev_node
                return #This way we delete only the first instance and we don't need to traverse the entire list
            else: #Inch-worm forward
                prev_node = curr_node
                curr_node = curr_node.get_next()
    
    def append(self, item):
        """Appends an item to the head (index -1) of the list"""
        if self.head == None:
            temp = Node(item)
            self.head = temp
            self.rear = temp
            self.length +=1
            return
        temp = Node(item)
        self.head.set_next(temp)
        temp.set_next(None)
        self.head = temp
        self.length +=1


    def insert(self, index:int, item):
        if index == 0: #If index is 0, we're just adding an item
            temp = Node(item)
            temp.set_next(self.rear)
            self.rear = temp
            if len(self)==0:
                self.head = temp
            self.length +=1
            return
        
        if index == self.length -1: #If we insert at head we need to make some modifications
            temp = Node(item)
            temp.set_next(None)
            self.head.set_next(temp)
            self.head = temp
            self.length +=1
            return
        
        curr_node = self.rear
        if 0>index or index>=self.length:
            raise IndexError("Insert index out of range")
        else:
            pos = 0 #Start traversing until we arrive at index's previous position
            while pos != index-1:
                curr_node = curr_node.get_next()
                pos +=1
            temp = Node(item) #Then we put the new node "on top" of that node
            temp.set_next(curr_node.get_next())
            curr_node.set_next(temp)
            self.length +=1
            return

    def index(self, item)->int:
        pos = 0
        if self.is_empty():
            raise ValueError()
        else: 
            curr_node = self.rear
        while curr_node.get_next() != None:
            if curr_node.get_data() == item:
                return pos
            else:
                pos +=1
                curr_node = curr_node.get_next()
        raise ValueError()

    def pop(self, index=0)->any:
        if 0>index or index>=self.length:
            raise IndexError("Pop index out of range")
        elif index == 0:
            temp = self.rear.get_data() #Store the value *before* changing rear
            self.rear = self.rear.get_next()
            self.length -=1
            return temp
        #As our list is singly linked we can't traverse backwards. pop() will be O(n)
        else:
            pos = 1
            prev_node =self.rear
            curr_node = self.rear.get_next() if not self.is_empty() else None
            while curr_node.get_next() != None:
                if pos == index:
                    prev_node.set_next(curr_node.get_next())
                    self.length-=1
                    return curr_node.get_data()
                else:
                    pos+=1
                    prev_node =curr_node
                    curr_node = curr_node.get_next()
            prev_node.set_next(None)
            self.head=prev_node #In case we pop the head we need to update it
            self.length-=1
            return curr_node.get_data()
        
"""
t = Node("a")
my_list = SinglyLinkedList()
print(my_list.is_empty())
    
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.is_empty())
print(len(my_list))
print(my_list)
print(31 in my_list)
print(-2 in my_list)
print("aaa",my_list.head.get_data())

my_list.remove(31)
print(len(my_list))
print(my_list)
my_list.add("aoidao")
print("aaa",my_list.head.get_data())

print(my_list)
my_list.append("ñojp")
print(my_list)
print(len(my_list))
my_list.insert(2, "insertao")
print(my_list)
my_list.insert(0, "insertao2")
print(my_list)
my_list.insert(8, "insertao3")
print(my_list)
print(my_list.head.get_data())
print(len(my_list))

print(my_list.index(54))
print(my_list)

print(my_list.pop(3))
print(my_list)
print(my_list.pop(len(my_list)-1))
print(my_list)
print(my_list.head.get_data())

print(my_list[-1])
my_list[0]=0
print(my_list)"""