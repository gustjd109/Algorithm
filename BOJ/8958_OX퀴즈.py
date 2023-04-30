import sys

T = int(sys.stdin.readline())

for i in range(T):
    A = str(sys.stdin.readline().rstrip())
    Sum = 0
    Cnt = 0

    for i in range(len(A)):
        if A[i] == 'O':
            Cnt += 1
            Sum += Cnt
        elif A[i] == 'X':
            Cnt = 0
            
    print(Sum)