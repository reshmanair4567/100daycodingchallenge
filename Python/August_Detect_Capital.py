class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        match1=True
        match2=True
        match3=True
        n=len(word)
        
        #all caps
        for i in range(n):
            if not word[i].isupper():
                match1=False
                break
        if match1:
            return True
        #no caps  
        for i in range(n):
            if word[i].isupper():
                match2 = False
                break
        if match2:
            return True
        #first cap
        for i in range(1,n):
            if not (word[0].isupper() and word[i].islower()):
                match3=False
                
        if match3:
            return True
        else:
            return False
        
            
        
if __name__=="__main__":
    inp=input()
    print(Solution().detectCapitalUse(inp))           
        
        