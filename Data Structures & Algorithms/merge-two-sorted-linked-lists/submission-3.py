# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        p1 = list1
        p2 = list2
        if not p1:
            return p2
        if not p2:
            return p1
        if p1.val < p2.val:
            cur = p1
            p1 = p1.next
        else:
            cur = p2
            p2 = p2.next
        head = cur
        while p1 or p2:
            if not p1:
                cur.next = p2
                return head
            if not p2:
                cur.next = p1
                return head
            if p1.val < p2.val:
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
        return head