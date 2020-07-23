class Solution:
    def get_sum(n):
        sum=0
        if n==0:
            pass
        while n>0:
            digit=n%10
            n=n//10
            sum+=digit**2
        print(sum)
        return sum
    
    def isHappy(self, n: int) -> bool:
        sum=Solution.get_sum(n)
        seen=set()
        while True:
            if sum==1:
                return True
            else:
                sum=Solution.get_sum(sum)
                if sum not in seen:
                    seen.add(sum)
                else:
                    return False
                    
        return False


if __name__=="__main__":
    num=int(input("enter a number"))
    result=Solution().isHappy(num)
    if result==True:
        print("a happy number")
    else:
        print("not a happy number")
