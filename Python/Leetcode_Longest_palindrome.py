from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=Counter(s)
        ans=0
        for i,v in d.items():
            ans+=int(v/2)*2
            if ans%2==0 and v%2==1:
                ans+=1          

        return ans

if __name__=="__main__":
    s="ccc"
    print("Longest Palindrome:  ",Solution().longestPalindrome(s))