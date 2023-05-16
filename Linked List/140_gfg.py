# Python program to reverse a linked list to given size
#reverse until doesnt work here but works in gfg
# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList


class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head
        next = None
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverseUntil(self,head,k):
        prev = None
        curr = head

        if(k<=1 or curr is None):
            return head

        i = 0
        next = None
        while (curr  and i < k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        head.next = self.reverseUntil(curr,k)
        return prev

 # Function to insert a new node at the beginning

    def push(self, new_data):
        if (self.head is None):
            new_node = Node(new_data)
            self.head = new_node
            self.head.next = None
        else:
            new_node = Node(new_data)
            curr = self.head
            while (curr.next is not None):
                curr = curr.next
            curr.next = new_node
            curr.next.next = None

    # Utility function to print the LinkedList
    def printList(self):
        print("**************")
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
        print("**************")

    def getHead(self):
        return self.head;

# Driver code
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)


print("Given linked list")
llist.printList()
llist.reverseUntil(llist.getHead(),3)
print("\nReversed linked list")
llist.printList()
