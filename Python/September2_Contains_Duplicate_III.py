class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # regular duplication
        if t == 0 and len(set(nums)) == len(nums):
            return False
        
        for i in range(len(nums)):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

'''OR'''
class Solution:

def containsNearbyAlmostDuplicate(self, nums, k, t):
    if k < 1 or t < 0:
        return False
    dic = collections.OrderedDict()
    for n in nums:
        key = n if not t else n // t
        for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
            if m is not None and abs(n - m) <= t:
                return True
        if len(dic) == k:
            dic.popitem(False)
        dic[key] = n
    return False