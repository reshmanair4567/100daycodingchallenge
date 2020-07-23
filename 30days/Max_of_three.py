def maximum_value(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    elif a==b==c:
        return "All numbers are equal"
    else:
        if a==b or b==c:
            if c>a or a<b:
                return c
            else:
                return a
        # if b==c:
        #     if a>b:
        #         return a
        #     else:
        #         return c
        if a==c:
            if b>a:
                return b
            else:
                return a



if __name__=="__main__":
    a=int(input())
    b=int(input())
    c=int(input())
    print("the maximum integer is {}".format(maximum_value(a,b,c)))