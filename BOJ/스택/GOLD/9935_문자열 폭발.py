import sys

sys.stdin = open("input.txt","rt")
S = sys.stdin.readline().strip()
bombString = list(sys.stdin.readline().strip())
bombStringLength = len(bombString)
stack = []

# 반복문을 통헤 문자열 탐색
for i in S:
    # 스택에 문자 삽입
    stack.append(i)
    # 스택의 맨 뒤에서 폭발 문자열 길이만큼 짜른 것의 문자열과 폭발 문자열이 같다면
    # 스택의 맨 뒤에서 폭발 문자열 길이만큼 문자열 삭제
    if stack[-bombStringLength:] == bombString:
        for _ in range(bombStringLength):
            stack.pop()

# 스택이 남아있다면 남은 스택 출력
if stack:
    print(''.join(stack))
# 스택이 비어있다면 "FRULA" 출력
else:
    print('FRULA')