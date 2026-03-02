from typing import Optional

class ListNode:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Solution:
    def middleOfLinkedList(self,head: Optional[ListNode]) -> ListNode:
        temp1=head
        temp2=head
        
        while temp2 != None and temp2.next != None:
            temp1=temp1.next
            temp2=temp2.next.next
        return temp1
    

def list_to_linkedlist(ls):
    head=ListNode(ls[0])
    temp=head
    for i in ls[1:]:
        temp.next=ListNode(i)
        temp=temp.next
    return head

def print_linkedlist(head:ListNode):
    temp=head
    while temp!=None:
        print(temp.value,end=' -> ')
        temp=temp.next
    print('None')


s=Solution()
l=[1,2,3,4,5]
head=list_to_linkedlist(l)
print_linkedlist(head)

res=s.middleOfLinkedList(head)
print("Middle of the linkedlist: ",res.value)