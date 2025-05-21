class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def distance_to_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            distance = 0
            while slow != fast:
                slow = slow.next
                fast = fast.next
                distance += 1
            return distance
    return -1
