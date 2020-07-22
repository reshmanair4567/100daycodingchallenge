class Solution:
    def singleNumber(nums):
        no_duplicate=[]
        for i in nums:
            if i not in no_duplicate:
                no_duplicate.append(i)
            else:
                no_duplicate.remove(i)
        return(no_duplicate.pop())
        
        
        '''for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=-1
                nums[i+1]=-1
        
        nums=sorted(nums)
        return(nums[-1])'''
    

if __name__=="__main__":
    nums=[2,2,1]
    s=Solution()
    print(s.singleNumber(nums)         