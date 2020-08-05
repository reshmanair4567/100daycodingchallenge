class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        rev=""
        for ele in s:
            if ele.isalnum():
                rev+=ele
                
            else:
                s.replace(ele,"")
        
        rev=list(rev)
        return(rev==rev[::-1])

        ''' Method 2 - O(n) Time complexity and Space complexity'''
        '''
        alpha_s=filter(lambda ch:ch.isalnum(),s)
        lower_s=list(map(lambda ch:ch.lower(),alpha_s))
       
        return(lower_s==lower_s[::-1])'''


if __name__=="__main__":
    s="A man, a plan, a canal: Panama"
    c=Solution()
    print(c.isPalindrome(s))