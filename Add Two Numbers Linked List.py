from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addLinkedList(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        iterator = ans
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, r = divmod(val1 + val2 + carry, 10)
            iterator.next = ListNode(r)
            iterator = iterator.next
        
        return ans







if __name__ == '__main__':
    a = Solution()
    b = ListNode(2)
    c = ListNode(3)
    d = b
    e = c
    for i in range(2):
        d.next = ListNode(i)
        e.next = ListNode(i+1)
        d = d.next
        e = e.next
    print(a.addLinkedList(b,c))


# Easy
# Linked List