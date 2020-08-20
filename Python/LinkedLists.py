class Node(object):
    def __init__(self,val,next):
        self.val=val
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            node=Node(data,self.head)
            self.head=node
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            itr=self.head
            listr=""
            while itr:
                listr+=str(itr.val)+"---->"
                itr=itr.next
        print(listr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)

    def insert_values(self,data_list):
        #to create a linked list from an input array
        self.head = None
        for data in data_list:
            #reverse of the provided list will be printed
            #self.inset_at_beginning(data)
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next   
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            
    def insert_at(self,index,data):
        itr=self.head
        if index<0 or index>=self.get_length():
            print("Invalid Index")
        if index==0:
            #self.head=Node(data,None)
            self.insert_at_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1

if __name__=="__main__":
    ll=LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(52)
    ll.insert_values(["apple","banana","chickoo","dragonfruit"])
    ll.insert_at(0,"figs")
    print("length of my linked list is : ",ll.get_length())
    ll.remove_at(2)
    ll.print()

    
        
'''
class Node:
    def __init__(self,val,next):
        self.val=val
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def add_beginning(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            s=Node(data,self.head)
            self.head=s
        
    def add_end(self,data):
        itr=self.head
        if itr is None:
            self.head=Node(data,None)
        else:
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)

    def delete_beginning(self):
        self.head=self.head.next

    
    def delete_end(self):
        itr=self.head
        while itr.next.next is not None:
            itr=itr.next
        itr.next=None

    
    def insertlist(self,listdata):
        
        for i in range(0,len(listdata)):
            if self.head is None:
                self.head=Node(listdata[0],None)
            else:
                itr=self.head
                while itr.next is not None:
                    itr=itr.next
                itr.next=Node(listdata[i],None)

            

    def insertlist2(self,listdata):
        self.head=None
        for i in listdata:
            self.add_end(i)
        
        
    def print_list(self):
        itr=self.head
        li=""
        if itr is None:
            print("Empty Linked List")
        else:
            while itr:
                li=li+str(itr.val)+"\t"
                itr=itr.next
            print(li)
                
                
                
if __name__=="__main__":
    
    l=LinkedList()
    l.insertlist([23,45,67,89,91,6,0,5])
    # l.add_beginning(20)
    # l.add_beginning(30)
    # l.add_end(40)
    l.print_list()
    # l.delete_beginning()
    # l.delete_end()
    # l.print_list()
    
'''


''' Leetcode_design_linked_list
class Node(object):
    def __init__(self,val,next):
        self.val=val 
        self.next=next
class LinkedList:
    def __init__(self):
        self.size=0
        self.head=None

    def insert_at_beginning(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            node=Node(data,self.head)
            self.head=node
    
    def get_length(self):
        self.size=0
        itr=self.head
        while itr:
            self.size+=1
            itr=itr.next
        return self.size

    def get_index(self,index):
        '''Get the value of index-th node in the linked list. If index is invalid , return -1'''
        if index<0 or index>=self.size:
            return -1
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr.val
        
    def insert_at_index(self,data,index):
        if index>=self.size:
            return
        if index<0:
            index=0
        if index==0:
            self.head=Node(data,None)
        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                    node=Node(data,itr.next)
                    itr.next=node
                itr=itr.next
                count+=1
    
    def delete_at_index(self,index):
        if index>=self.size or index<0:
            return "Invalid Index"
        if index==0:
            self.head=self.head.next
        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                    itr.next=itr.next.next
                    break
                count+=1
                itr=itr.next

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            itr=self.head
            listr=""
            while itr:
                listr+=str(itr.val)+"--->"
                itr=itr.next
        print("Linked List is: "+str(listr))

if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(66)
    ll.insert_at_beginning(22)
    ll.insert_at_beginning(33)
    ll.insert_at_beginning(44)
    ll.insert_at_beginning(11)
    ll.insert_at_beginning(77)
    ll.insert_at_beginning(88)
    ll.insert_at_end(55)
    ll.print()
    print("Length of the Linked List: "+str(ll.get_length()))
    ll.insert_at_index(34,3)
    ll.print()
    print("Length of the Linked List: "+str(ll.get_length()))
    ll.delete_at_index(3)
    ll.print()
    print("Length of the Linked List: "+str(ll.get_length()))
    print("Value at the Index element is:   "+str(ll.get_index(6)))
'''


'''
Sort a Linked List:
    def getMiddle(self):
        if self.head is None:
            return self.head
        slow=self.head
        fast=self.head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next   
        return slow

    def sortedMerge(self,left,right):
        result=0
        if left==None:
            return right
        if right==None:
            return left
        if left.val<=right.val:
            result=left
            result.next=self.sortedMerge(left.next,right)
        else:
            result=right
            result.next=self.sortedMerge(left,right.next)
        return result
        

    def mergesort(self,h):
        if h==None or h.next==None:
            return h
        else:
            middle=self.getMiddle()
            nexttomiddle=middle.next
            middle.next=None

            #apply mergesort on left list
            left=self.mergesort(h)
            #apply mergesort on right list
            right=self.mergesort(nexttomiddle)

            #merge left and right list
            sortedList=self.sortedMerge(left,right)
            return sortedList
'''