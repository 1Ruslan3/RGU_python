class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    tmp = LinkedList()
    cur = tmp 

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next

        cur = cur.next

    if l1:
        cur.next = l1

    if l2: 
        cur.next = l2

    return tmp.next

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(4)

l2 = LinkedList(1)
l2.next = LinkedList(3)
l2.next.next = LinkedList(4)

res = mergeTwoLists(l1, l2)

while res:
    print(res.val)
    res = res.next
