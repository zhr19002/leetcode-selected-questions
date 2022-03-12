class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

def list2link(list_):
    while len(list_) != 0:
        head = ListNode(list_[0])
        cur = head
        for i in range(1,len(list_)):
            cur.next = ListNode(list_[i])
            cur = cur.next
        return head
    return None

def link2list(link):
    list_ = []
    dummy_head = ListNode(next_=link)
    cur = dummy_head
    while cur.next:
        list_.append(cur.next.val)
        cur = cur.next
    return list_

class Solution:
    def getIntersectionNode(self, headA, headB):
        headA = list2link(headA)
        headB = list2link(headB)
        
        if len(link2list(headA)) > len(link2list(headB)):
            step = len(link2list(headA)) - len(link2list(headB))
            fast, slow = headA, headB
        else:
            step = len(link2list(headB)) - len(link2list(headA))
            fast, slow = headB, headA
        while step:
            fast = fast.next
            step -= 1
        
        while fast.val != slow.val:
            fast = fast.next
            slow = slow.next
            if fast == None:
                return None
        return fast.val

s = Solution()
print(s.getIntersectionNode([4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5]))
print(s.getIntersectionNode([0, 9, 1, 2, 4], [3, 2, 4]))
print(s.getIntersectionNode([2, 6, 4], [1, 5]))