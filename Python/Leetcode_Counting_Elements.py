class Solution:
    def countElements(self, arr):
        count=0
        '''for ele in arr:
            if ele+1 in arr:
                count+=1
                  
        return count'''
        sset=set(arr)
        for ele in arr:
            if ele+1 in sset:
                count+=1
        return count


if __name__=="__main__":
    arr=[1,1,2,3]
    s=Solution().countElements(arr)
    print(s)