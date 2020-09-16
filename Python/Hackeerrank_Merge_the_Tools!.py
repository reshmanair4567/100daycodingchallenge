def merge_the_tools(string, k):
    # your code goes here
    count=0
    while string:
        s=string[0:k]
        seen=''
        
        for c in s:
            if c not in seen:
                seen+=c
        print(seen)
        count+=1
        string=string[k:]
    print(count)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)