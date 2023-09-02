S = input()
result = 0
stack = []

for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
    else:
        if S[i - 1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)