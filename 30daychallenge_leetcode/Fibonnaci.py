def Fibonnaci(n):
    if n<0:
        print("Enter valid input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:  
        return(Fibonnaci(n-1)+Fibonnaci(n-2))

if __name__=="__main__":
    n=7
    print(Fibonnaci(n))
