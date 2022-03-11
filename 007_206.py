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
    def reverseList(self, head):
        head = list2link(head)
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return link2list(pre)

s1 = Solution()
print(s1.reverseList([1, 2, 3, 4, 5]))