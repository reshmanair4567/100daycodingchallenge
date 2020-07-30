'''nums=[1,2,3,0,0,5,7,9]
nums.remove(0)
print(nums)
for i in range(len(nums)):
    if nums[i]==0:
        nums.remove(nums[i])
        nums.append(0)
print(nums)
'''
from collections import Counter
class Solution:
	def compress(self, chars: List[str]) -> int:
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
        return len(chars)

