def horizontal(n):
    str=" "
    for i in range(n):
        str=str+" " + "---"
    print(str)

def vertical(n):
    st=" "
    for i in range(n+1):
        st=" | "+ " "+ st
    print(st)


if __name__=="__main__":
    size=int(input())
    for i in range(size):
        horizontal(size)
        vertical(size)
    horizontal(size)   #smart point

