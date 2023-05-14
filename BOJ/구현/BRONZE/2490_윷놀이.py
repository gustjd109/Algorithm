# 0의 개수를 기준으로 푸는 방법
import sys

sys.stdin = open("input.txt","rt")
for _ in range(3):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr.count(0) == 1:
        print('A')
    elif arr.count(0) == 2:
        print('B')
    elif arr.count(0) == 3:
        print('C')
    elif arr.count(0) == 4:
        print('D')
    else:
        print('E')

# 배와 등의 숫자를 모두 더한 값을 기준으로 푸는 방법
import sys

sys.stdin = open("input.txt","rt")
for _ in range(3):
    arr = sum(list(map(int, sys.stdin.readline().split())))
    if arr == 3:
        print('A')
    elif arr == 2:
        print('B')
    elif arr == 1:
        print('C')
    elif arr == 0:
        print('D')
    else:
        print('E')