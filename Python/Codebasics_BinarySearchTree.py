class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            #add value to left sub tree
            if self.left:  # if left element exists, add element recursively 
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            #add valuye to right sub tree
            if self.right:  # if an element exists, add element recursively 
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements=[]

        #visit left tree
        if self.left:
            elements+=self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            #val might be in left sub tree
            if self.left :
                return self.left.search(val)
            else:
                return False

        if val>self.data:
            #val might be in right sub tree
            if self.right :
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=="__main__":
    nums=[17,4,-1,20,9,23,18,-1,4,20,20,20,20,34]
    numbers_tree=build_tree(nums)
    x=numbers_tree.in_order_traversal()
    print("Inorder Traveresed BST is:  ",x)
    print("Miniumum number is BST :    ",min(x))
    print("Maximum number in BST:      ",max(x))
    print("Sum of all elements in BST: ",sum(x))
    print(" Is 4 in the list ? :       ",numbers_tree.search(4))
