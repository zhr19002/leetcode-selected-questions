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
    def removeNthFromEnd(self, head, n):
        head = list2link(head)
        dummy_head = ListNode(next_=head)
        fast = dummy_head
        slow = dummy_head             
        while n:
            fast = fast.next
            n -= 1
            
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next    

        return link2list(dummy_head.next)

if __name__ == '__main__':
    s = Solution()
    print(s.removeNthFromEnd([1, 2, 3, 4, 5], 2))
    print(s.removeNthFromEnd([1], 1))
    print(s.removeNthFromEnd([1, 2], 1))
