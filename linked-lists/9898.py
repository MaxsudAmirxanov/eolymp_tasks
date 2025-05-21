class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sum_linked_list(head):
    total = 0
    current = head
    while current:
        total += current.val
        current = current.next
    return total
