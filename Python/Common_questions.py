'''Palindrome or Not'''
def palindrome(s):
    return s==s[::-1]

if __name__=="__main__":
    s="malayalam"
    print(palindrome(s))

''' Reverse a digit / Palindrome Digit'''

def palindrome_digit(nums):
    d=abs(nums)
    reverse=0
    while d!=0:
        reverse=reverse*10+d%10
        d=d//10
    if nums>=0:
        return reverse==nums
    else:
        return False

if __name__=="__main__":
    nums=-121
    print("Palindrome Digit: ",palindrome_digit(nums))