#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr=head
        vals=[]
        while curr:
            vals.append(curr.val)
            curr=curr.next
        ans=0
        for i in vals:
            ans+=pow(2,i)
        return ans

        
