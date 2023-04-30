import sys

N = N2 = int(sys.stdin.readline())
cyclecnt=0

while True:
    first_num = N // 10
    second_num = N % 10
    sum_num = (first_num + second_num) % 10
    N = (second_num * 10) + sum_num
    cyclecnt += 1
    if N == N2:
        break
print(cyclecnt)