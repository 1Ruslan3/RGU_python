class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
        tmp = LinkedList(0)
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