#Iterative##
def Fibonnaci(n):
    a=0
    b=1
    if n<0:
        print("please enter valid input")
    if n==0:
        return a
    if n==1:
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
    return b

'''
#Recursion
def Fibonnaci(n):
    if n<0:
        print("Enter valid input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:  
        return(Fibonnaci(n-1)+Fibonnaci(n-2))'''

if __name__=="__main__":
    n=9
    print(Fibonnaci(n))
