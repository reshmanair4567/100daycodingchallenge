def stringShift(s, shift):
    st=[]
    for ch in s:
        st.append(ch)
    if len(s)==0:
        return None
    for direction,amount in shift:
        if direction==0:
            while amount>0:
                x=st.pop(0)
                st.append(x)
                amount-=1
        elif direction==1:
            while amount>0:
                st.insert(0,st.pop(-1))
                amount-=1
                        
                        
    return("".join(st))
                        


'''
for direction,amount in shift:
            amount %=len(s)
            if direction==0:
                #move necessary amount of characters from start to end
                s=s[amount:] + s[:amount]
            else:
                #move necessary amount of characters from end to start 
                s=s[-amount:]+s[:-amount]
        return s
    '''

if __name__=="__main__": 
    s="abc"
    shift = [[0,1],[1,2]]
    print(stringShift(s,shift))