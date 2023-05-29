def detectLoop(head):
    #Initialize both slow and fast to head
    slow = head
    fast = head

    #Check if fast is not none and push fast 2 steps and slow 1 step.
    #If there is a loop fast will be equal to slow and we will return True.
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    
    return False