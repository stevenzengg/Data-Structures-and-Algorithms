from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        step = 2
        while step < len(lists):
            for i in range(0, len(lists)-1, step):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+int(step/2)])
            
            step *= 2
        
        return lists[0]

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        iterator = ans

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            if val1 > val2:
                iterator.next = val2
                val2 = val2.next
            else:
                iterator.next = val1
                val1 = val1.next
            
        if l1:
            iterator.next = l1
        elif l2:
            iterator.next = l2

        return ans.next







if __name__ == '__main__':
    a = Solution()
    b = ListNode(0)
    c = ListNode(0)
    d = b
    e = c
    for i in range(2):
        d.next = ListNode(i)
        e.next = ListNode(i+1)
        d = d.next
        e = e.next
    
    print(a.mergeKLists(b,c))


# Easy
# Linked List