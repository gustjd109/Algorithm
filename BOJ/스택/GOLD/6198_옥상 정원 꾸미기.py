# 해당 문제는 아래와 같이 이중 for 문을 이용하면 시간 초과가 발생한다.
# import sys

# sys.stdin = open("input.txt","rt")
# N = int(sys.stdin.readline())
# buildings = [int(sys.stdin.readline()) for _ in range(N)]
# ans = 0

# for i in range(N - 1):
#     for j in range(i + 1, N):
#         if buildings[j] >= buildings[i]:
#             break
#         elif buildings[j] < buildings[i]:
#             ans += 1

# print(ans)

# 해당 문제는 모든 빌딩을 순차적으로 탐색하며, 아래와 같은 조건에 따라 현재 탐색하고 있는 빌딩의 높이를 스택에 삽입한다.
# 현재 탐색하고 있는 빌딩의 높이가 스택의 TOP보다 크거나 같다면, 현재 탐색하고 있는 빌딩의 높이가 TOP보다 작아질때까지 스택의 TOP을 삭제한다.
# 현재 탐색하고 있는 빌딩의 높이가 스택의 TOP보다 작으면, 스택에 존재하는 빌딩 수 - 1만큼 결과에 더해준다.
# 현재 탐색하고 있는 빌딩의 높이를 스택에 삽입한다.
import sys

sys.stdin = open("input.txt","rt")
N = int(sys.stdin.readline())
buildings = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
stack = []

for i in range(N):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()

    stack.append(buildings[i])
    ans += len(stack) - 1

print(ans)