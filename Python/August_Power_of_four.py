import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num==1:
            return True
        elif num>2 and num<2**31:
            powo=int(math.log(num,10)/math.log(4,10))
            x=pow(4,powo)
            if x==num:
                return True
        return False
            

if __name__ =="__main__":
    num=64
    print(Solution().isPowerOfFour(num))