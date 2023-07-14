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

    def find_min(self):
        curr_node = self
        while curr_node.get_left_child():
            curr_node = curr_node.left_child
        return curr_node

        """if self.get_left_child(): recursive way of doing it: it does incur on overhead
            return self.left_child.find_min()
        else:
            return self"""

    def find_succesor(self):
        return self.right_child.find_min() #This function, as far as the excercises in the book are concerned, is only used to help delete nodes in
                #a specific case: when the node has both children. So it is not necesary to cover the posibility of it not having a right children
    def splice_out(self): #Remember that this function is to be used when a node has a maximum of 1 child
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.get_left_child():
            if self.is_left_child():
                self.parent.left_child = self.left_child
            else:
                self.parent.right_child = self.left_child
            self.left_child.parent = self.parent
        else:
            if self.is_left_child():
                self.parent.left_child = self.right_child
            else:
                self.parent.right_child = self.right_child
            self.right_child.parent = self.parent

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


    def delete(self, k):
        if self.size > 1:
            node_to_delete = self._get(k, self.root)
            if node_to_delete:
                self.remove(node_to_delete)
                self.size -=1
            else:
                raise KeyError()
        elif self.size == 1 and self.root.key == k:
            self.root = None
            self.size -=1
        else:
            raise KeyError()


    def __delitem__(self, k):
        self.delete(k)

    def remove(self, node_to_remove: TreeNode):
        if node_to_remove.is_leaf(): #If the node is a leaf we just need to remove the parent's link to it
            if node_to_remove.parent.left_child == node_to_remove:
                node_to_remove.parent.left_child = None
            else:
                node_to_remove.parent.right_child = None
        elif node_to_remove.has_both_chilren():
            succ = node_to_remove.find_succesor()
            succ.splice_out()
            node_to_remove.key = succ.key
            node_to_remove.payload = succ.payload
        else:
            if node_to_remove.get_left_child():
                if node_to_remove.is_left_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.left_child
                elif node_to_remove.is_right_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.left_child
                else:
                    node_to_remove.replace_node_data(node_to_remove.left_child.key, node_to_remove.left_child.payload, node_to_remove.left_child.left_child, node_to_remove.left_child.right_child)
            else:
                if node_to_remove.is_left_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.right_child
                elif node_to_remove.is_right_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                else:
                    node_to_remove.replace_node_data(node_to_remove.right_child.key, node_to_remove.right_child.payload, node_to_remove.right_child.left_child, node_to_remove.right_child.right_child)


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
