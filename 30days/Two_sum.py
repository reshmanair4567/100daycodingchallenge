def two_sum(nums,target):
    a={}
    for i,v in enumerate(nums):
        n=target-v
        if n not in a:
            a[v]=i
        else:
            print([a[n],i])

if __name__=="__main__":
    nums=[2,7,9,11,13]
    n=9
    two_sum(nums,n)


