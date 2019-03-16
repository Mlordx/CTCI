def hanoi(A,B,C,n):
    if n == 0: return

    if n == 1:
        C.push(A.pop())
        return

    hanoi(A,C,B,n-1)

    C.push(A.pop())

    hanoi(B,A,C,n-1)
