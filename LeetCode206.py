class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def recurcive_trace(self, node, prev):
        if not node.next:
            node.next = prev
            return node
        reversed_head = self.recurcive_trace(node.next,node)
        node.next = prev
        return reversed_head
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        reversed_head = self.recurcive_trace(node = head.next,prev = head)
        head.next = None
        return reversed_head

a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(4)
a.next.next.next = ListNode(7)
a.next.next.next.next = ListNode(1)
a.next.next.next.next.next = ListNode(2)
a.next.next.next.next.next.next = ListNode(6)

b = Solution()
print(b.reverseList(a))