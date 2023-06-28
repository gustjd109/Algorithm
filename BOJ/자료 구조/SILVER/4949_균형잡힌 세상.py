# 해당 문제는 스택을 이용항 간단하게 풀 수 있는 문제이다.
# while 문을 이용하여 문자열을 계속 입력받고, 해당 문자열이 '.'이라면 break 문을 통해 반복을 빠져나온다.
# 아니라면, for 문을 이용하여 입력 받은 문자열의 각 문자를 탐색하면서 해당 문자가 '('이거나 '['라면 스택에 삽입한다.
# 문자가 ')'이거나 ']'라면, 스택에 저장된 마지막 문자를 삭제한다.
# 이때, 스택은 비어있지 않아야 하고, 스택의 마지막 문자가 각 괄호의 짝과 맞아야 삭제할 수 있도록 조건을 추가해 줘야 한다.
# 만약, 괄호와 짝이 아니라면 스택에 해당 문자를 삽입하고 break 문을 통해 반복문을 빠져나온다.
# 마지막으로, 스택의 길이가 0, 즉 비어있다면 해당 문자열은 균형을 이루고 있으므로 'yes'를 출력하고, 아니면 'no'를 출력한다.
# 주의사항으로는 문자열을 입력받을 때, rstrip()을 이용하여 오른쪽 공백을 없애줘야 '출력 초과'과 발생하지 않고, 문제를 맞힐 수 있다.

import sys

sys.stdin = open("input.txt","rt")

while(1):
    S = sys.stdin.readline().rstrip()
    stack = []

    if S == '.':
        break

    for i in S:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')