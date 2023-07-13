class BinaryTree:
    def __init__(self, root) -> None:
        self.key = root #This isn't the payload: this tree is very basic
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp
    
    def insert_right(self,new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def set_root_val(self, val):
        self.key = val

    def get_root_val(self):
        return self.key
    
    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


r = BinaryTree("a")

print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())
r.get_right_child().insert_left("nooo")

def show_tree(t:BinaryTree, ):
    res = ""
    res += str(t.get_root_val())
    
    if t.get_left_child() != None:
        res +="["
        res += show_tree(t.get_left_child())
        res +="]"
    if t.get_right_child() != None:
        res +="["
        res += show_tree(t.get_right_child())
        res +="]"

    return res
print("aa")
print(show_tree(r))
r.preorder()