class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def length_linked_list(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length
