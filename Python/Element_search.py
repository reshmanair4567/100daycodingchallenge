def element(li,age):
    flag=False
    if age in li:
        flag = True
    return flag

if __name__=="__main__":
    li=list(range(1,21))
    age=17
    print(element(li,age))
