class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

def list2link(list_, pos):
    while len(list_):
        list_ += 10 * list_[pos:]
        head = ListNode(list_[0])
        cur = head
        for i in range(1, len(list_)):
            cur.next = ListNode(list_[i])
            cur = cur.next
        return head
    return None

class Solution:
    def detectCycle(self, head, pos):
        head = list2link(head, pos)
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast.val == slow.val:
                while head.val != slow.val:
                    head = head.next
                    slow = slow.next
                return head.val
        return None

if __name__ == '__main__':
    s = Solution()
    print(s.detectCycle([3, 2, 0, -4], 1))
    print(s.detectCycle([1, 2], 0))
