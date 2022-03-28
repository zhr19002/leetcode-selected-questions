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
    def swapPairs(self, head):
        head = list2link(head)
        dummy_head = ListNode(next_=head)
        pre = dummy_head
        
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next
            cur.next = post.next
            post.next = cur
            pre.next = post
            pre = pre.next.next
        return link2list(dummy_head.next)

s = Solution()
print(s.swapPairs([1, 2, 3, 4]))
print(s.swapPairs([]))
print(s.swapPairs([1]))
