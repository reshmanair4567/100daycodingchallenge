def unique_characters(s):
    n=len(s)
    for i in range(n):
        if s.count(s[i])==1:
            return i
    return -1

if __name__=="__main__":
    s="lleetcode"
    print(unique_characters(s))
    
