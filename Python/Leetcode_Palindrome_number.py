def palindrome(nums):
    if nums<0:
        return False
    else:
        reverse=0
        digit=abs(nums)
        while digit!=0:
            reverse=reverse*10+digit%10
            digit=digit//10
        return reverse==nums


if __name__=="__main__":
    nums=int(input("What's your number:  "))
    print(palindrome(nums))