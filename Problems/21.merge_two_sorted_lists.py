from lc import *


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    # build linked-lists from nested python lists using helper from lc.py
    l1 = make_list([1, 2, 4])
    l2 = make_list([1, 3, 4])
    merged = s.mergeTwoLists(l1, l2)
    # convert the result back to a python list for easy printing
    print(list_to_array(merged))
