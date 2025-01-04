class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertAtEnd(self, linkedList : ListNode, val : int):
        while linkedList.next :
            linkedList = linkedList.next
        newNode = ListNode(val)
        linkedList.next = newNode
        return linkedList
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        rootNode = ListNode()
        if list2 is None and list1 is None:
            return None
        if list1 is not None and list2 is None:
            return list1
        if list2 is not None and list1 is None:
            return list2
        while list1 or list2:
            if list1 == None and list2 != None:
                pass
            elif list2 == None and list1 != None:
                pass
            else:
                if list1.val == list2.val:
                    pass
                elif list1.val >  list2.val:
                    pass
                else:
                    pass 
            