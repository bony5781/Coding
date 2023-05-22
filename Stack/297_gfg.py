class Queue:
    def __init__(self):
        self.q1 = []
    
    def enqueue(self,data):
        self.q1.append(data);

    def dequeue(self):
        self.q1.pop(0)
    
    def isEmpty(self):
        if len(self.q1)==0: 
            return True 
        else: return False
    
    def traverse(self):
        for i in range(len(self.q1)):
            print(f"{self.q1[i]} ",end="")
        print("")
    
q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.traverse()
q.dequeue()
q.traverse()
print(q.isEmpty())