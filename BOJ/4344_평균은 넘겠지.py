import sys

C = int(sys.stdin.readline())

for i in range(C):
    Scores = list(map(int, sys.stdin.readline().split()))
    Sum = 0
    Avg = 0
    Cnt = 0
    Per = 0

    for j in Scores[1:]:
        Sum += j
    Avg = Sum / Scores[0]

    for j in Scores[1:]:
        if j > Avg:
            Cnt += 1
    Per = Cnt / Scores[0] * 100

    print(f'{Per:.3f}%')