import sys

barcket = list(sys.stdin.readline())
stack = []
answer = 0
tmp = 1

for i in range(len(barcket)):
    if barcket[i] == '(':
        stack.append(barcket[i])
        tmp *= 2
    elif barcket[i] == '[':
        stack.append(barcket[i])
        tmp *= 3
    elif barcket[i] == ')':
        if stack == [] or stack[-1] == '[':
            answer = 0
            break
        # stack리스트가 아닌 원래 리스트인 barcket리스트에서 i - 1인덱스 괄호가 한쌍을 이루지 않으면
        # tmp값만 2로 나누고 stack에서 괄호 하나를 삭제
        elif barcket[i - 1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()
    elif barcket[i] == ']':
        if stack == [] or stack[-1] == '(':
            answer = 0
            break
        # stack리스트가 아닌 원래 리스트인 barcket리스트에서 i - 1인덱스 괄호가 한쌍을 이루지 않으면
        # tmp값만 3로 나누고 stack에서 괄호 하나를 삭제
        elif barcket[i - 1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()

if stack:
    answer = 0

print(answer)