import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    H  = int(sys.stdin.readline())
    # 스택이 비어있지 않고 스택의 마지막 값이 입력받은 값보다 작거나 같으면
    # 스택의 마지막 값을 삭제한다.
    # 스택이 비어있거나, 스택의 마지막 값이 입력받은 값보다 크면
    # 스택에 입력받은 값을 삽입힌다. 
    while stack and stack[-1] <= H:
        stack.pop()
    stack.append(H)

#스택에 남아있는 막대기의 길이를 출력한다.
print(len(stack))