class linkedListNode:
    def __init__(self, value, next =  None):
        self.value = value
        self.next = next

class linkedList:
    def merge(self, list1, list2):
        merged = linkedListNode(0)
        current = merged
        while list1 and list2:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return merged.next
    
    def printLinkedList(self, head):
        current = head
        while current is not None:
            print(current.value, end = " -> ")
            current = current.next
        print("None")

head1 = None
tail1 = None

while True:
    value = input("Enter value for list 1 or stop: ")
    if value.lower() == "stop":
        break
    newNode = linkedListNode(int(value))

    if head1 is None:
        head1 = newNode
        tail1 = newNode
    else:
        tail1.next = newNode
        tail1 = newNode

head2 = None
tail2 = None

while True:
    value = input("Enter value for list 2 or stop: ")
    if value.lower() == "stop":
        break
    newNode = linkedListNode(int(value))
    if head2 is None:
        head2 = newNode
        tail2 = newNode
    else:
        tail2.next = newNode
        tail2 = newNode

ll = linkedList()
merged = ll.merge(head1, head2)
ll.printLinkedList(merged)