class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = LinkedList(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        digit = total % 10
        carry = total // 10

        current.next = LinkedList(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

l1 = LinkedList(2)
l1.next = LinkedList(4)
l1.next.next = LinkedList(3)
l2 = LinkedList(5)
l2.next = LinkedList(6)
l2.next.next = LinkedList(4)

result = addTwoNumbers(l1, l2)

while result is not None:
    print(result.val)
    result = result.next