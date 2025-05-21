class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def cycle_length(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = 1
            current = slow.next
            while current != slow:
                length += 1
                current = current.next
            return length
    return 0
