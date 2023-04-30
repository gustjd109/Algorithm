import sys

def SortNum(Num):
    for i in range(len(Num) - 1):
        for j in range(i + 1, len(Num)):
            if Num[i] > Num[j]:
                Num[i], Num[j] = Num[j], Num[i]

N = int(sys.stdin.readline())
Num = []

for i in range(N):
    Num.append(int(sys.stdin.readline()))

SortNum(Num)

for i in Num:
    print(i)