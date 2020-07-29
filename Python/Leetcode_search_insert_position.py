def position(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
        else:
             
           

if __name__=="__main__":
    nums=[1,3,5,6]
    target=4
    print(position(nums,target))