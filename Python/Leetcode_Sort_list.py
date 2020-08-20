#Sort a Linked List - Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
                
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))


#------------------------------------ OR --------------------


# merge sort, recursively 
def sortList(self, head):
    if not head or not head.next:
        return head
    # divide list into two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    # cut down the first part
    slow.next = None
    l = self.sortList(head)
    r = self.sortList(second)
    return self.merge(l, r)
    
# merge in-place without dummy node        
def merge(self, l, r):
    if not l or not r:
        return l or r
    if l.val > r.val:
        l, r = r, l
    # get the return node "head"
    head = pre = l
    l = l.next
    while l and r:
        if l.val < r.val:
            l = l.next
        else:
            nxt = pre.next
            pre.next = r
            tmp = r.next
            r.next = nxt
            r = tmp
        pre = pre.next
    # l and r at least one is None
    pre.next = l or r
    return head