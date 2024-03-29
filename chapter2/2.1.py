def removeDuplicates(head):
    if head is None: return
    
    seen = {head.value : True}

    aux = head

    while aux.nextNode is not None:
        aux2 = aux.nextNode
        if seen.get(aux2.value) is not None:
            aux.nextNode = aux2.nextNode
            del aux2
        else:
            seen[aux2.value] = True
        aux = aux.nextNode

    return head

def removeDuplicates2(head): #no extra buffers
    if head is None: return
    
    current = head

    while current is not None:
        val = current.value
        
        runner = head
        while runner.nextNode is not current:
            if runner.value == val: runner.nextNode = runner.nextNode.nextNode
            else: runner = runner.nextNode
            
        current = current.nextNode

    return head
