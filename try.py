class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def push(self,data):
        if self.head is None:
            new_node=Node(data);
            self.head=new_node;
            self.head.next=None;
        else:
            curr=self.head;
            while(curr.next is not None):
                curr=curr.next;
            new_node=Node(data);
            curr.next=new_node;
            curr.next.next=None;

    def print(self):
        print("*****************");
        curr=self.head;
        while(curr is not None):
            print(curr.data);
            curr=curr.next;
        print("*****************");
        
    def reverse(self):
        prev=None;
        curr=self.head;
        next=None;
        while(curr is not None):
            next=curr.next;
            curr.next=prev;
            prev=curr;
            curr=next;
        self.head=prev;

ll=LinkedList();
ll.push(30);
ll.push(40);
ll.push(50);
ll.push(60);
ll.print();
ll.reverse();
ll.print();