def kth(head,k): #assuming it is kth from last
    pointer = head.nextNode #first element
    while pointer is not None: size++

    if k >= size: return

    pointer = head.nextNode
    for i in range(size-k): pointer = pointer.nextNode

    return pointer
