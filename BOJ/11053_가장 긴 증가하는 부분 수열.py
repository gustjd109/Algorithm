# 이진 탐색을 이용한 풀이
# 최장 증가 부분 수열의 최대 길이는 구할 수 있으나, 수열값을 도출하는 데에는 사용할 수 없음
import sys

def binary_search(start, end, value):
    while start <= end:
        mid = (start + end) // 2

        if stack[mid] >= value:
            end = mid - 1
        else:
            start = mid + 1
    return start

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# 부분 수열이 오름차순으로 저장될 리스트(A 리스트의 제일 처음 값을 넣어준다)
stack = [A[0]]

# A 리스트의 제일 처음 값을 stack 리스트를 넣어줬기 때문에 인덱스를 1~N-1까지 반복
for i in range(1, N):
    # A[i]값이 stack 리스트의 마지막 값보다 크면 stack 리스트에 삽입
    if A[i] > stack[-1]:
        stack.append(A[i])
    # 작으면 이진 탐색을 통해 stack 리스트에서 A[i]을 삽입할 수 있는 A[i]보다 크면서 가장 작은 값의 인덱스를 찾는다.
    else:
        max_low_index = binary_search(0, len(stack) - 1, A[i])
        # 찾은 인덱스의 값과 A[i]값을 바꾼다.
        stack[max_low_index] = A[i]

print(len(stack))

#########################################################################################################

# 동적 계획법을 이용한 풀이(3주차에 동적으로 해결하는 문제로 동일한 문제가 있음)
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# A[i]를 마지막 값으로 가지는 가장 긴 증가 부분 수열의 길이 1로 초기화
DP = [1] * N

for i in range(N):
    for j in range(i):
        # a[i]가 A[j]보다 크면 DP[i]에 DP[i]와 DP[j] + 1을 비교하여 더 큰 값을 저장
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))