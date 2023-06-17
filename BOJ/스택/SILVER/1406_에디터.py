# 해당 문제는 두 개의 스택을 이용하여 풀 수 있다.
# 커서를 기준으로 왼쪽 스택과 오른쪽 스택 두 개를 생성한다.
# 오른쪽 스택은 방향을 뒤집어져있으므로, pop하면 왼쪽에 있는 원소가 삭제되고, append하면 왼쪽에 원소가 삽입된다.
# 커서는 항상 왼쪽 스택의 맨 오른쪽에 위치하므로, 왼쪽 스택에 문자를 순서대로 삽입한다.
# if ~ elif 문을 이용하여 각 명령어를 수행한다.
# P 명령어 : $원소를 왼쪽 스택에 삽입
# L 명령어 : 왼쪽 스택의 마지막 원소를 삭제하고, 해당 원소를 오른쪽 스택에 삽입(왼쪽 스택이 비어있으면 무시)
# D 명령어 : 오른쪽 스택의 마지막 원소를 삭제하고, 해당 원소를 왼쪽 스택에 삽입(오른쪽 스택이 비어있으면 무시)
# B 명령어 : 커서는 항상 왼쪽 스택의 맨 오른쪽에 위치하므로, 왼쪽 스택의 마지막 원소를 삭제
# 모든 명령어를 수행했으면, 왼쪽 스택과 뒤집힌 오른쪽 스택을 더해 join 라이브러리 함수를 이용하여 공백없이 문장으로 출력한다.

import sys

sys.stdin = open("input.txt","rt")
left = list(sys.stdin.readline().strip())
right = []

for i in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == 'L' and left:
        right.append(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

print(''.join(left + right[::-1]))