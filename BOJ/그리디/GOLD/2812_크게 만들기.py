import sys

N, K = map(int,sys.stdin.readline().split())
nums = list(sys.stdin.readline().strip())
stack = []
k = K

for num in nums:
    # 스택이 비어있지 않고 / K값이 0 크고 / 스택의 마지막 수가 nums의 i번째 수보다 작을때까지
    # 스택에 저장된 수를 삭제하고, k값을 -1시켜줌
    while stack and stack[-1] < num and k > 0:
        stack.pop()
        k -= 1
    # 반복문이 종료되면 num값을 스택에 저장
    stack.append(num)

print(''.join(stack[:N - K]))