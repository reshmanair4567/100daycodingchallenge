from collections import Counter
class Solution:
    def findDuplicates(self, nums):
        n=Counter(nums)
        ans=[]
    
        for i,v in n.items():
            if v>1:
                ans.append(i)
        return ans
'''Method-2
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}                    # used for key lookups only
        ret = []                  # store duplicates
        for num in nums:
            if num not in d:
                d[num] = True     # store a bool to minimize space
            else: 
                ret.append(num)
        return ret
'''

if __name__=="__main__":
    nums=[2,3,4,1,3,2,2,7,5,1]
    c=Solution().findDuplicates(nums)
    print(c)