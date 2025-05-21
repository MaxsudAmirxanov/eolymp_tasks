class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_first_element(head):
    if head:
        return head.next
    return None
