# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        head = curr = ListNode()
        for value in values:
            curr.next = ListNode(value)
            curr = curr.next
        return head.next

    def to_list(self):
        values = []
        curr = self
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

    def __str__(self):
        return str(self.to_list())
