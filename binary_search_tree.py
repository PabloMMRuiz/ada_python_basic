class TreeNode:

    def __init__(self,key, val, left = None, right = None, parent = None) -> None:
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def is_left_child(self):
        return self.parent and self.parent.get_left_child() == self
    
    def is_right_child(self):
        return self.parent and self.parent.get_right_child() == self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.right_child or self.left_child)
    
    def has_children(self): #What is the use of this?
        return not self.is_leaf()

    def has_both_chilren(self):
        return self.left_child and self.right_child
    
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

#So why use Search Trees when we have binary search? Because in Python lists, insertion is O(n), and in linked list, traversal is.
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def __len__(self)->int:
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def _put(self, key, val, curr_node:TreeNode):
        if key < curr_node.key:
            if curr_node.get_left_child():
                self._put(key, val, curr_node.get_left_child())
            else:
                curr_node.left_child = TreeNode(key, val, parent=curr_node)
        elif key > curr_node.key:
            if curr_node.get_right_child():
                self._put(key, val, curr_node.get_right_child())
            else:
                curr_node.right_child = TreeNode(key, val, parent=curr_node)
        elif key == curr_node.key:
            curr_node.payload = val
    def put(self, key, val):
        if self.root == None:
            self.root = TreeNode(key, val)
        else: 
            self._put(key, val, self.root)
        self.size +=1

    def __setitem__(self, k, v):
        self.put(k,v)

    def _get(self, key, curr_node: TreeNode)->TreeNode:
        if not curr_node:
            return None
        elif curr_node.key == key:
            return curr_node
        elif key < curr_node.key:
            return self._get(key, curr_node.get_left_child())
        else:
            return self._get(key, curr_node.get_right_child())
    
    def get(self, key):
        if self.root:
            res =  self._get(key, self.root)
        if res:
            return res.payload
        else:
            raise KeyError()
    
    def __getitem__(self, k):
        return self.get(k)
    
    def __contains__(self, k):
        if self._get(k, self.root):
            return True
        else:
            return False

tester = BinarySearchTree()
tester[1] = "unoo"
tester[2] = "doos"
tester[-2] = "menosdos"
tester[-1.5] = "madre"
print(tester[-1.5])
tester[-1.5] = "feoanfoinf"
print(tester[-1.5])
print(12 in tester)
print(1 in tester)