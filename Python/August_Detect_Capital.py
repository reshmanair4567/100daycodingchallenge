class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        match1=True
        match2=True
        match3=True
        n=len(word)

        '''Method 1'''
        #all caps
        if word[0].isupper() and word[1].isupper():
            for i in range(2,n):
                if word[i].isupper():
                    match1=True
                else:
                    match1=False
            if match1:
                return True
            else:
                return False
        else:
            #one start caps or no caps 
            if word[0].isupper():
                for i in range(1,n):
                    if word[i].islower():
                        match2=True
                    else:
                        match2=False
                if match2:
                    return True
                else:
                    return False

            else:
                for i in range(n):
                    if word[i].isupper():
                        match3=False
                    else:
                        match3=True
                if match3:
                    return True
                else:
                    return False
        
        
            
            

                



            



        '''
        Method 2 
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
        if not word[0].isupper():
            match3=False
        if match3:
            for i in range(1,n):
                if word[i].isupper():
                    match3=False

        if match3:
            return True
        else:
            return False
        
    '''  
        
if __name__=="__main__":
    inp=input()
    print(Solution().detectCapitalUse(inp))           
        
        