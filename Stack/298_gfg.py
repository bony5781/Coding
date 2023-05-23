#Function to push an integer into the stack1.
def push1(a,x):
    a.insert(0,x)
    
#Function to push an integer into the stack2.
def push2(a,x):
    a.insert(len(a),x)
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    if(a):
        return a.pop(0)
    return -1
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    if(a):
        return a.pop(len(a)-1)
    return -1

