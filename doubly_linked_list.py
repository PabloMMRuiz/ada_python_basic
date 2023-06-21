class DoubleLinkNode():
    def __init__(self, init_data) -> None:
        self.data = init_data
        self.next = None
        self.back = None

    def get_data(self)->any:
        return self.data
    
    def get_next(self):
        return self.next
    
    def get_back(self):
        return self.back
    
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_back(self, new_back):
        self.back = new_back

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0 #So len operation is linear. Could be solved with traversing: small memory improvement at greater time cost
    def __len__(self)->int:
        return self.length

    def __contains__(self, item)->bool:
        curr_node = self.head
        while curr_node != None:
            if curr_node.get_data() == item:
                return True
            curr_node = curr_node.get_next()
        
        return False

    def __str__(self) -> str:
        if self.is_empty():
            return ""
        res = str(self.head.get_data())
        curr_node = self.head.get_next()
        while curr_node != None:
            res = res +", "+ str(curr_node.get_data())
            curr_node = curr_node.get_next()
        return "["+res+"]"
    
    def __getitem__(self, index):
        if type(index) == int:
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
        """elif type(index) == slice:
            if index.step  == 0:
                raise ValueError("Slice step cannot be zero")
            elif (index.step > 0 and index.start>index.stop) or (index.step < 0 and index.start < index.stop):
                temp = SinglyLinkedList()
                return temp
            else:
                #First we transform start and stop to positive, in-range ints
                if index.start < 0 :
                    if index.start < -self.length:
                        index.start = 0
                    if index.stop > self.length-1:
                        index.stop = self.length-1
                    """
        #TODO: Implement true slicing
    def __setitem__(self, index, item):
        if -self.length >=index or index>=self.length:
            raise IndexError("Index out of range")
        elif 0<=index: 
            pos = 0
            curr_node = self.head
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            curr_node.set_data(item)
        else: 
            index = self.length + index #Index is negative here
            pos = 0
            curr_node = self.head
            while pos != index:
                pos +=1
                curr_node =curr_node.get_next()
            curr_node.set_data(item)

    def is_empty(self)->bool:
        return self.head == None
# [1,2,3,4,5]: 1 is head, 5 is head
    def add(self, item):
        """Pushes an item to the head (index 0) of the list"""
        temp = DoubleLinkNode(item)
        if self.is_empty():
            temp.set_back(temp)
            temp.set_next(None)
            self.head = temp
        else:
            temp.set_back(self.head.get_back())
            temp.set_next(self.head)
            self.head.set_back(temp)
            self.head = temp
        self.length +=1
    
    def remove(self, item):
        curr_node = self.head
        while curr_node !=None:
            if curr_node.get_data() == item:
                curr_node.get_back().set_next(curr_node.get_next())
                curr_node.get_next().set_back(curr_node.get_back())
                self.length -=1
                return
            else:
                curr_node = curr_node.get_next()
        raise ValueError()
    
    def append(self, item):
        """Links an item to the end (index -1) of the list"""
        temp = DoubleLinkNode(item)
        if self.is_empty():
            temp.set_back(temp)
            temp.set_next(None)
            self.head = temp
        else:
            temp.set_back(self.head.get_back())
            self.head.get_back().set_next(temp)
            self.head.set_back(temp)
        self.length +=1


    
    def insert(self, index:int, item):
        if index == 0: #If index is 0, we're just adding an item
            self.add(item)
            return
        if index == self.length: #If we insert at last+1 position, it's appending 
            self.append(item)
            return
        
        curr_node = self.head
        if -self.length>index or index>self.length:
            raise IndexError("Insert index out of range")
        else:
            if index < 0:
                index = self.length + index
            pos = 0 #Start traversing until we arrive at index's previous position
            while pos != index-1:
                curr_node = curr_node.get_next()
                pos +=1
            temp = DoubleLinkNode(item) #Then we put the new node "on top" of that node
            temp.set_next(curr_node.get_next())
            temp.set_back(curr_node)
            temp.get_next().set_back(temp)
            curr_node.set_next(temp)
            self.length +=1
            return
        
    
    def index(self, item)->int:
        pos = 0
        if self.is_empty():
            raise ValueError()
        else: 
            curr_node = self.head
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
            temp = self.head #Store the value *before* changing head
            self.head = self.head.get_next()
            if self.is_empty():
                self.length = 0
                return #We don't want to accidentally run the next method on None if we popped from a lenght 1 list
            self.head.set_back(temp.get_back()) 
            self.length -=1
            return temp.get_data()
        #When the list was singly linked we couldn't traverse backwards. pop("-1") was be O(n)
        #Now we have double link so pop will be o(1) at first and last element, and O(n) at the rest
        elif index == self.length -1:
            temp = self.head.get_back()
            temp.get_back().set_next(None)
            self.head.set_back(temp.get_back())
            self.length -=1
            return temp.get_data()
        else:
            pos = 0
            curr_node = self.head
            while pos < index:
                    curr_node = curr_node.get_next()
                    pos +=1
                    #Traverse to the node we are going to pop
            curr_node.get_back().set_next(curr_node.get_next())
            curr_node.get_next().set_back(curr_node.get_back())
            self.length -=1
            return curr_node.get_data()
            
a = DoublyLinkedList()
a.add("hola")
a.add(2)
a.add("ofoih")
print(a)
a.remove(2)
print(a)
a.insert(0, "primero")
a.insert(3, "ultimo")
print(a)
a.insert(1, "tumadre")
print(a)
a.remove("tumadre")
print(len(a))
print(a)
print(a.index("hola"))
print(a.pop())
print(a)
print(a.pop(len(a)-1))
print(a)
a.insert(1, "osjbnafpifiuh")
print(a)
print(a.pop(1))
print(a)
