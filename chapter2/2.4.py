def sumLists(n1,n2):
    one = 0
    p1 = n1 #no head
    p2 = n2
    res = new Node(-1)

    while (p1 is not None) and (p2 is not None): #sum up to the smallest number
        sum_ = p1.value + p2.value + one
        if sum_ >= 10:
            sum_ = sum_%10
            one = 1
        else: one = 0

        res.nextNode = new Node(sum_)
        p1 = p1.nextNode
        p2 = p2.nextNode
        res = res.nextNode

    if p1 is not None: #rest of the digits of the biggest number
        while p1 is not None:
            sum_ = p1.value + one
            if sum_ == 10:
                sum_ = 0
                one = 1
            else: one = 0

            res.nextNode = new Node(sum_)
            p1 = p1.nextNode
            res = res.nextNode
    elif p2 is not None:
        while p2 is not None:
            sum_ = p2.value + one
            if sum_ == 10:
                sum_ = 0
                one = 1
            else: one = 0

            res.nextNode = new Node(sum_)
            p2 = p2.nextNode
            res = res.nextNode
        
    if one: res.nextNode = new Node(1)
    return res
