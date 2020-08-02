from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

    def print(self):
        print(self.container)


if __name__=="__main__":
    s=Stack()
    string1=input("enter here")
    #print(s.peek())
    # sizee=s.size()
    # #print(sizee)

    for i in string1:
        s.push(i)
    rev=""
    while s.is_empty()!=True:
        rev+=s.pop()
    print(rev)


    


    



    
    
