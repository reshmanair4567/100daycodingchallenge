
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
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)

    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    
    def get_length(self):
        self.size=0
        itr=self.head
        while itr:
            self.size+=1
            itr=itr.next
        return self.size

    def middle_linked_list(self):
        mid=int(self.size//2)
        itr=self.head
        mll=[]
        for _ in range(mid):
            itr=itr.next
        else:
            mll=[]
            while itr:
                mll.append(itr.val)
                itr=itr.next
        print(mll)

    def palindrome(self):
        listp=[]
        itr=self.head
        while itr:
            listp.append(itr.val)
            itr=itr.next
        return (listp==listp[::-1])

    def get_index(self,index):
        if index<0 or index>self.size:
            return -1
        else:
            itr=self.head
            for _ in range(index):
                itr=itr.next
            return itr.val

    def remove_node(self,data):
        curr=self.head
        prev=None
        while curr:
            if curr.val==data:
                self.head=curr.next
                return
            prev=curr
            curr=curr.next
            if curr.val==data:
                prev.next=curr.next
                return
            

    def print(self):
        itr=self.head
        listr=""
        while itr:
            listr+=str(itr.val)+"-->"
            itr=itr.next
        print(listr)


if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(35)
    ll.insert_at_beginning(45)
    ll.insert_at_beginning(55)
    ll.insert_at_beginning(95)
    ll.insert_at_beginning(65)
    ll.insert_at_end(11)
    ll.print()
    ll.reverse()
    ll.print()
    print("Length of Linked List: "+str(ll.get_length()))
    ll.middle_linked_list()
    print("Palindrome result: "+str(ll.palindrome()))
    print("Value at given index is: "+str(ll.get_index(2)))
    ll.remove_node(35)
    ll.print()
    print("Length of Linked List: "+str(ll.get_length()))





            






































'''
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
    
    def insert_at_the_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)

    def get_length(self):
        self.size=0
        itr=self.head
        while itr:
            self.size+=1
            itr=itr.next
        return self.size
    
    def get_index(self,index):
        if index<0 or index>=self.size:
            return -1
        else:
            itr=self.head
            for _ in range(index-1):
                itr=itr.next
            return itr.val

    def delete_all_duplicates(self):
        dup={}
        prev=None
        curr=self.head
        while curr:
            if curr.val in dup:
                prev.next=curr.next
            else:
                dup[curr.val]=1
                prev=curr
            curr=prev.next

    def middle_linked_list(self):
        itr=self.head
        for _ in range(int(self.size/2)):
            itr=itr.next
        else:
            listm=[]
            while itr:
                listm.append(itr.val)
                itr=itr.next
        return listm

    def reverse(self):
        prev=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    def palindrome(self):
        listp=[]
        itr=self.head
        while itr:
            listp.append(itr.val)
            itr=itr.next
        return (listp==listp[::-1])

    def delete_at_index(self,index):
        if index<0 or index>=self.size:
            return -1
        if index==0:
            self.head=self.head.next

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            itr=self.head
            listr=""
            while itr:
                listr+=str(itr.val)+"---->"
                itr=itr.next
            print("The Linked List is: "+str(listr))

if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(16)
    ll.insert_at_beginning(45)
    ll.insert_at_beginning(47)
    ll.insert_at_the_end(6)
    ll.print()
    print("Length of Linked list: "+str(ll.get_length()))
    print("Element at the requested Index is: "+str(ll.get_index(0)))
    ll.delete_all_duplicates()
    ll.print()
    print("Middle of Linked List: "+str(ll.middle_linked_list()))
    ll.reverse()
    ll.print()
    print("Palindrome or Not: "+str(ll.palindrome()))
'''

'''
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

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)
    
    def get_length(self):
        self.size=0
        itr=self.head
        while itr:
            self.size+=1
            itr=itr.next
        return self.size
    
    def get_index(self,index):
        if index<0 or index>=self.size:
            return -1
        else:
            curr=self.head
            for _ in range(index):
                curr=curr.next
        return curr.val
    
    def insert_at_index(self,data,index):
        if index<0 or index>=self.size:
            return "Invalid index"
        if index==0:
            node=Node(data,None)
        else:
            curr=self.head
            for _ in range(index-1):
                curr=curr.next
            node=Node(data,curr.next)
            curr.next=node
    
    def remove_at_index(self,index):
        if index<0 or index>=self.size:
            return -1
        if index==0:
            self.head=self.head.next
        else:
            itr=self.head
            for _ in range(index-1):
                itr=itr.next
            itr.next=itr.next.next

    def middle(self):
        itr=self.head
        listr=[]
        for _ in range(int(self.size/2)):
            itr=itr.next
        else:
            listr=[]
            while itr:
                listr.append(itr.val)
                itr=itr.next
        return listr

    def reverse_linkedlist(self):
        prev=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    def palindrome_linked_list(self):
        itr=self.head
        listp=[]
        while itr:
            listp.append(itr.val)
            itr=itr.next
        return listp==listp[::-1]

    def single_consecutive_remove_duplicates(self):
        itr=self.head
        while itr.next is not None:
            curr1=itr.val
            curr2=itr.next.val
            if curr1==curr2:
                itr.next=itr.next.next
            itr=itr.next

    def remove_all_duplicates(self):
        prev=None
        curr=self.head
        dup={}
        while curr:
            if curr.val in dup:
                prev.next=curr.next
            else:
                dup[curr.val]=1
                prev=curr
            curr=prev.next
             
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        listr=""
        itr=self.head
        while itr:
            listr+=str(itr.val)+"--->"
            itr=itr.next
        print("Linked List is "+str(listr))

if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(12)
    ll.insert_at_end(12)
    ll.insert_at_beginning(11)
    ll.insert_at_beginning(14)
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(15)
    ll.insert_at_end(17)
    ll.print()
    # print("Length of the Linked List: "+str(ll.get_length()))
    # ll.insert_at_index(34,3)
    # ll.print() 
    # print("Length of the Linked List: "+str(ll.get_length()))   
    # ll.remove_at_index(3)   
    # ll.print()    
    # print("Length of the Linked List: "+str(ll.get_length()))  
    # print(ll.middle())
    # ll.reverse_linkedlist()
    # ll.print()
    # print(ll.palindrome_linked_list())
    # ll.single_consecutive_remove_duplicates()
    # ll.print()
    # ll.remove_all_duplicates()
    # ll.print()  '''