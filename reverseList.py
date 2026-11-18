class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if head is None or head.next is None:
        return head
    
    p = head
    c = p.next
    n = c.next

    p.next = None

    while n is not None:
        c.next = p
        p = c
        c = n
        n = n.next

    c.next = p
    return c 
    
a = LinkedList(1)
b = LinkedList(2)
c = LinkedList(3)
d = LinkedList(4)
a.next = b
b.next = c
c.next = d

r = reverseList(a)
print(r.val)
