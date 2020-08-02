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
    string1=input("enter your input:  ")

    for ch in string1:
        s.push(ch)
    
    s.print()
    st=[]
    
    values={ "[":"]","{":"}","(":")" }
    for ch in string1:
        if ch in values:
            st.append(ch)
        elif st and values[st[-1]]==ch:
            st.pop()
            
    if len(st)==0:
        print("balanced")
    else:
        print("not balanced")
