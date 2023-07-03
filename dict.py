class HashTable: #This is our dict implementation
    def __init__(self) -> None:
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def hash_value(self, key, size)->int:
        #Auxiliary function for hash location
        return key%size
    
    def rehash(self, initial_pos, size):
        return (initial_pos+1)%size

    def put(self, key, value):
        hash_pos = self.hash_value(key, self.size) 
        if self.slots[hash_pos] == None:
            self.slots[hash_pos] = key
            self.data[hash_pos] = value
        elif self.slots[hash_pos] == key:
            self.data[hash_pos] = value #if the key already exists, we replace the value
        else:
            next_pos = hash_pos
            iters = 0
            while self.slots[next_pos] != None and self.slots[next_pos] != key and iters <= self.size:
                next_pos = self.rehash(next_pos, self.size)
                iters +=1
            if self.slots[next_pos] == None:
                    self.slots[next_pos] = key
                    self.data[next_pos] = value
                    return
            elif self.slots[next_pos] == key:
                    self.data[next_pos] = value
                    return
            raise MemoryError("Hash table full") #The book makes the assumption that we'll always have empty space. 
            #I assume we do not. If the table is full, it will alert so. This should also allow for an easier size growth implementation


    def get(self, key)->any:
        start = self.hash_value(key, self.size)
        pos = start
        if self.slots[pos] != key and self.slots[pos] != None:
            pos = self.rehash(pos, self.size)
        elif self.slots[pos] == key:
            return self.data[pos]
        else:
            raise KeyError("Key not found")
        while self.slots[pos] != None:
            if self.slots[pos] == key:
                return self.data[pos]
            elif self.slots[pos] == None:
                raise KeyError("Key not found") #The book just returns None, but I chose to follow python's implementation ideas
            elif pos == start:
                raise KeyError("Key not found")
            else:
                pos = self.rehash(pos, self.size)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)

    def delete(self, key):
        start = self.hash_value(key, self.size)
        pos = start
        while self.slots[pos] != None:
            if self.slots[pos] == key:
                self.slots[pos] = None
            elif self.pos == None:
                return
            elif pos == start:
                return
            else:
                pos = self.rehash(pos, self.size)
    def __contains__(self, key)->bool:
        try:
            self.get(key)
            return True
        except:
            return False #Really dirty implementation, but works
        
    def __str__(self) -> str:
        res = "{"
        for key, item in zip(self.slots, self.data):
            if key != None:
                temp = f"{str(key)}: {str(item)}, " #Not the most beautiful finish. But will do
                res +=temp
        res += "}"
        return res
"""    
h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[10] = "fish" #Since slot 10 is full it'll go to the next empty one: 0
h[54] = "elephant"
print(h)
"""