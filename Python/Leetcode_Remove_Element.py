nums=[0,1,2,2,3,0,4,2]
n=len(nums)
val=2
no_seen=[]
for ele in nums:
    if ele!=val:
        no_seen.append(ele)

print(len(no_seen))




