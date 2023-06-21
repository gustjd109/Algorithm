import sys

sys.stdin = open("input.txt","rt")
n = int(sys.stdin.readline())
stack, result, flag = [], [], True
now = 1 # 스택에 삽입할 현재 값

for i in range(n):
    num = int(sys.stdin.readline())
    
    # 스택에 삽입할 현재 값이 입력받은 num 값보다 클때까지 삽입
    while now <= num:
        stack.append(now)
        result.append('+')
        now += 1

    # 스택의 마지막 값이 num 값과 같은 경우 해당 값 스택에서 삭제
    if stack[-1] == num:
        stack.pop()
        result.append('-')

    # 스택의 마지막 값이 num 값보다 큰 경우(수열을 만들 수 없는 경우) flag를 False로 변경
    else:
        flag = False

# 수열을 만들 수 없는 경우 NO 출력
if flag == False:
    print('NO')
# 수열을 만들 수 있는 경우로 위의 모든 과정을 완료하고, result 스택의 모든 값(+ or -) 출력
else:
    for i in result:
        print(i)