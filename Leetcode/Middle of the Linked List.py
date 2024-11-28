# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        fast_ptr, slow_ptr = head, head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

# Manually create the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Find the middle node
middle = Solution().middleNode(head)

# Print all nodes starting from the middle
current = middle
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
