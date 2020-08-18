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
        print("Length of the Linked List: "+str(self.get_length()))

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
    ll.insert_at_index(34,3)
    ll.print()
    print("Value at the Index element is:   "+str(ll.get_index(6)))
