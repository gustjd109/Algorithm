# 해당 문제는 6198번 옥상 정원 꾸미기 문제와 비슷한 방법으로 풀 수 있다.
# 오큰수가 없으면, -1을 출력해야 하므로 -1로 초기화된 정답을 출력할 result 배열을 하나 생성한다.
# 아래 조건에 따라 입력받은 수들을 순차적으로 탐색한다.
# 스택이 비어있지 않고, A[스택 맨위]의 값이 A[i]의 값보다 작으면 반복문을 반복 수행한다.
# - result 배열의 stack.pop()한 인덱스 자리에 A[i] 값을 삽입한다.
# 스택이 비어있으면, 스택에 A[i]를 삽입한다.

import sys

sys.stdin = open("input.txt","rt")
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
result = [-1] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)