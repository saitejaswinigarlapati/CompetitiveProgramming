
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        res = [0]*len(vals)
        stack = []
        for i,val in enumerate(vals):
            while stack and val>vals[stack[-1]]:
                idx = stack.pop()
                res[idx] = val
            stack.append(i)
        return res
    
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_linkedlist(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    
head = [2,7,4,3,5]
head = list_to_linkedlist(head)

print("Linked List:")
print_linkedlist(head)

sol = Solution()
result = sol.nextLargerNodes(head)

print("Next Greater Nodes:", result)