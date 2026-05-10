class linkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linkedList:
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def printLinkedList(self, head):
        current = head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

head = None
tail = None

while True:
    value = input("Enter value or stop: ")
    if value.lower() == "stop":
        break
    newNode = linkedListNode(value)
    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode

ll = linkedList()
ll.printLinkedList(head)
middle = ll.findMiddle(head)
if middle:
    print("Middle node is:", middle.value)
else:
    print("List is empty")