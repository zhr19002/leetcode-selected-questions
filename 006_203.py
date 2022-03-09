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
    def removeElements(self, head, val):
        head = list2link(head)
        dummy_head = ListNode(next_=head)
        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return link2list(dummy_head.next)

s1 = Solution()
print(s1.removeElements([1, 2, 6, 3, 4, 5, 6], 6))
s2 = Solution()
print(s2.removeElements([], 1))
s3 = Solution()
print(s3.removeElements([7,7,7,7], 7))