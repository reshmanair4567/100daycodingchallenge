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

    
        

    