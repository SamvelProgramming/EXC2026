class linkedListNode:
    def __init__(self, value, next =  None):
        self.value = value
        self.next = next

class linkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        newNode = linkedListNode(value)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def printLinkedList(self):
        current = self.head
        while current is not None:
            print(current.value, end = " -> ")
            current = current.next
        print("None")

ll = linkedList()

while True:
    value = input("Enter value or stop: ")

    if value.lower() == "stop":
        break

    ll.insert(value)

ll.printLinkedList()