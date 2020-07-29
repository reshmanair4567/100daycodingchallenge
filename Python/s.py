nums=[1,2,3,0,0,5,7,9]
nums.remove(0)
print(nums)
'''
for i in range(len(nums)):
    if nums[i]==0:
        nums.remove(nums[i])
        nums.append(0)
print(nums)
'''
