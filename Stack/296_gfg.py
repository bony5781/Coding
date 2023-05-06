class Stack:
    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack) == 0
     
    def push(self, item):
        self.stack.append(item)
        print("Pushed item: ", item)

    def pop(self):
        if (self.check_empty()):
            print("Stack is empty")
            return "stack is empty"

        print("\nDeleted item : ", self.stack.pop())

    def print_stack(self):
        if (self.check_empty()):
            print("Stack is empty")
            return "stack is empty"
        
        for i in self.stack:
                print(f"{i} ",end='')

    def peek(self):
        return self.stack[len(self.stack)-1]

t1 = Stack()
print(t1.check_empty())
t1.push(50)
t1.push(27)
t1.push(30)
t1.print_stack()
t1.pop()
t1.print_stack()
print(f"\n{t1.peek()}")