def reverse_number(nums):
    if (nums<=2**31 or nums>=2**31-1):
        reverse=0
        digit=abs(nums)
        while digit!=0:
            reverse=reverse*10+digit%10
            digit=digit//10
        if nums>1:
            return reverse
        else:
            return -1*reverse
    else:
        return 0


if __name__=="__main__":
    nums=int(input("Enter the number you wish to reverse"))
    print(reverse_number(nums))
