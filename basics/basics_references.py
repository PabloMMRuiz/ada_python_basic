#Pyhton references

if __name__ == "__main__":
    print("Running...")
    list1 = [1,2,3]
    A=[list1]*3 #This builds a triple (3) reference to list1
    B=list1*3 #This builds a list repeating list1 three times. It doesn´t contain any reference to list1
    print("A\n", A)
    print("B\n", B)
    print("See ids at work:")
    print("A ", id(A))
    print("A's element 0",id(A[0]))
    print("list1 ", id(list1))
    print("B " , id(B))
    print("B's element 0" , id(B[0]))
    list1[2]=17
    print("A\n", A)
    print("B\n", B)
    A[0][0]=41
    print("list1\n",list1) #The elements in A are "literally" list1: changing one affects the original and thus all references. Unless type changes(see below)
    print("A\n", A)
    list1[2]=57 #As list1 type wasn´t changes, the reference is not lost. 
    print("A\n", A)
    print("B\n", B)


    var1 = [23]
    var2 = [var1]*3
    print(type(var1))
    print("var2\n", var2)
    print("var1 ",id(var1))
    print("var2's element 0 ",id(var2[0]))
    var1[0]=18
    print("var2\n", var2)
    var1=0 #If the referred object´s type changes, the reference is lost, and var2 becomes independent
    print(type(var1))
    print("var1 ", id(var1)) #As expected, memory direction changes if variable's type does
    print("var2's element 0 ",id(var2[0])) #This remains pointing at the old direction, now being "the only pointer"
    print("var2\n", var2)
 

#https://www.pythontutorial.net/advanced-python/python-references/ a bit of extra material