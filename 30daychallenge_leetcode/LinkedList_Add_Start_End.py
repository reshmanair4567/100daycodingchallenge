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
    
                
                
        
    
        
        