class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def count_nodes(self, head: ListNode) -> int:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None  # If the list has 0 or 1 node, return None

        length = self.count_nodes(head)
        middle = length // 2
        
        dummy = ListNode(0)  # Create a dummy node
        dummy.next = head
        prev = dummy
        
        for _ in range(middle):
            print(prev.val)
            prev = prev.next
        
        
        prev.next = prev.next.next  # Skip the middle node
        
        return dummy.next  # Return the actual head

a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(4)
a.next.next.next = ListNode(7)
a.next.next.next.next = ListNode(1)
a.next.next.next.next.next = ListNode(2)
a.next.next.next.next.next.next = ListNode(6)

b = Solution()
print(b.deleteMiddle(a))