class MinHeap:
    def __init__(self) -> None:
        self.items = [None]
        self.size = 0 #This is because that None is only used for the integer division of the bubble up algorithm: it is not part of the tree
    
    def bubble_up(self, i):
        while i//2 > 0:
            if self.items[i] < self.items[i//2]:
                self.items[i], self.items[i//2] = self.items[i//2], self.items[i]
            i = i//2
        #This is all due to the completeness of the tree: the height of the tree is about log(n) with n = len(items)
        #While one may think that just using something similar to binary search and a normal list structure is better, the need for insertion would
        #make it too inefficient
    
    def insert(self, k):
        self.items.append(k)
        self.size +=1
        self.bubble_up(self.size) #No need to substract thanks to the first item not being counted. Real length of the list (self.items) is one more than given


    def bubble_down(self, i):
        while i*2 <= self.size:
            mc = self.minimum_child(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc
    def minimum_child(self, i):
        if i*2+1 > self.size:
            return i*2 #Case where there is only 1 child
        
        elif self.items[i*2] < self.items[i*2+1]:
            return i*2
        
        else:
            return i*2+1
        
    def del_min(self):
        res = self.items[1]
        self.items[1] = self.items[self.size]
        self.size -=1
        self.items.pop()
        self.bubble_down(1) #As we pop the last element it is O(1)
        return res
    

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.size = len(a_list)
        self.items = [0] + a_list[:]
        while (i > 0):
            self.bubble_down(i)
            i = i - 1
            #Doing this we bubble down all nodes, thus effectively ordering the tree
