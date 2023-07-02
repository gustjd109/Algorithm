import sys

sys.stdin = open("input.txt","rt")
N = int(sys.stdin.readline())
num = 2

while N != 1:
    if N % num == 0:
        print(num)
        N /= num
    else:
        num += 1