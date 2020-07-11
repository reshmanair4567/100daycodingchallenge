from collections import Counter
def compress_string(s):
    d={}
    d=Counter(s)
    for i,v in d.items():
        print(i,v,sep="",end=""),

if __name__=="__main__":
    s="abbbbbbaaacccccccccccccccdddddddpppppp"
    compress_string(s)


