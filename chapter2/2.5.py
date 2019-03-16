def findLoop(head):
    fast = head
    slow = head

    while True:
        if fast is None or slow is None: return None

        slow = slow.nextNode
        fast = fast.nextNode.nextNode

        if slow == fast: break

    slow = head

    while True:
        slow = slow.nextNode
        fast = fast.nextNode
        if slow == fast: return slow

    return
