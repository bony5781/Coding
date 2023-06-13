# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

#Node Class
class Node:

    def __init__(self,data):
        self.data=data;
        self.next=None;

class LinkedList:

    def __init__(self):
        self.head=None

    def reverse(self):
        prev = None;
        curr = self.head;
        next = None;
        while (curr is not None):
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        self.head = prev;

 # Function to insert a new node at the beginning
    def push(self, new_data):
        if(self.head is None):
            new_node = Node(new_data)
            self.head = new_node;
            self.head.next = None;
        else:
            new_node = Node(new_data)
            curr = self.head;
            while(curr.next is not None):
                curr = curr.next;
            curr.next = new_node;
            curr.next.next = None;
    
    def pop(self,head):
        self.head = self.head.next;
    
    # Utility function to print the LinkedList
    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data);
            curr = curr.next;
        print("Done")

# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print ("Given linked list")
llist.printList()
llist.reverse()
print ("\nReversed linked list")
llist.printList()