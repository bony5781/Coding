class Stack:
    def __init__(self):
        self.s1 = []

    def push(self, item):
        self.s1.append(item)
        print(f"Pushed item = {item}")

    def pop(self):
        print(f"Item removed = {self.s1.pop()}")

    def traverse(self):
        i = 0
        while i < len(self.s1):
            print(f"{self.s1[i]} ", end="")
            i += 1

    def isEmpty(self):
        return len(self.s1) == 0

    def peek(self):
        if (self.isEmpty()):
            print("list is Empty")
        top = len(self.s1)-1
        print(f"Topmost element = {self.s1[top]}")
        return top


s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.pop()
s.traverse()
print(f"\n{s.isEmpty()}")
s.peek()
