class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_reverse(head):
    if head:
        print_reverse(head.next)
        print(head.val)
