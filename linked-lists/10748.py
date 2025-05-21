class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None
            return
