# 일반적인 풀이
import sys

sys.stdin = open("input.txt","rt")
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
mul_nums_list = list(str(A * B * C))
for i in range(0, 10):
    cnt = 0
    for j in mul_nums_list:
        if int(j) == i:
            cnt += 1
    print(cnt)

# count 함수를 이용한 풀이
import sys

sys.stdin = open("input.txt","rt")
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
mul_nums_list = list(str(A * B * C))

for i in range(10):
    print(mul_nums_list.count(str(i)))