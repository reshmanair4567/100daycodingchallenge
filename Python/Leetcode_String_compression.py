''' if we want the solution for ["a","a","a","a","b","b","c","c","a","a"] to look like ["a","4","b","2","c","a","2"] use technique one. this idle compression technique'''
class Solution:
    def compress(self, chars):
        groups=[]
        for ch in chars:
            if not groups or groups[-1][0]!=ch:
                groups.append([ch,1])
            else:
                groups[-1][1]+=1
        chars.clear()
        for g in groups:
            chars.append(g[0])
            if g[1]>1:
                for c in str(g[1]):
                    chars.append(c)
        print(chars)
        return len(chars)


if __name__=="__main__":
    chars=["a","a","b","b","c","c","c","a"]
    print(Solution().compress(chars))



'''2nd approach
 if we want the solution for ["a","a","a","a","b","b","c","c","a","a"] to look like ["a","6","b","2","c"]'''
from collections import Counter
class Solution2:
    def compress(self, chars):
        if len(chars)==0: 
            return 0
        elif len(chars)==1:
            return 1
            
        else:
            d=Counter(chars)
            ans=[]
            for i,v in d.items():
                if v>1:
                    ans.extend([i,str(v)])
                
                else:
                    ans.append(i)
        del chars[:]
        chars.extend(ans)
        print(chars)
        return len(chars)

if __name__=="__main__":
    chars=["a","a","b","b","c","c","c","a"]
    print(Solution2().compress(chars))


''' Outputs:
['a', '2', 'b', '2', 'c', '3', 'a']
7
['a', '3', 'b', '2', 'c', '3']
6'''