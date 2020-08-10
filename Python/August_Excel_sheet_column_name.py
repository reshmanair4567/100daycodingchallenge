class Solution:
    def titleToNumber(self, s: str) -> int:
        result=0
        for c in s:
            d=ord(c)-ord('A')+1
            result=result*26+d
        return result


if __name__=="__main__":
    s="AA"
    print(Solution().titleToNumber(s))