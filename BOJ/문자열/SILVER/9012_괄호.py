import sys

T = int(sys.stdin.readline())

for i in range(T):
    cnt = 0
    PS = sys.stdin.readline()
    for j in PS:
        if j == "(":
            cnt += 1
        elif j == ")":
            cnt -= 1
        if cnt < 0: # 자꾸 틀린 주범(스택에 아무것도 없는데 삭제할 경우)
            break
    if cnt == 0:
        print('YES')
    else:
        print("NO")