def two_sum(nums,target):
    seen={}
    for i,v in enumerate(nums):
        n=target-v
        if n not in seen: 
            seen[v]=i
        else:
            return [seen[n],i]

if __name__=="__main__":
    nums = [2, 7, 11, 15]
    target=9
    print(two_sum(nums,target))
