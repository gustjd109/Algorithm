import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))
# 탑의 인덱스와 값을 저장할 리스트
stack = []
# 각각의 탐들에서 발사한 레이저 신호를 수신한 탑들의 번호를 저장할 리스트
answer = []

# 탑의 수만큼 반복문 수행
for i in range(N):
    # 스택이 비어있지 않은 경우에 반복문 수행
    while stack:
        # 스택에 저장된 마지막 탑의 높이가 입력받은 탑의 높이보다 크거나 같으면
        # 탑 번호 저장 리스트에 스택에 저장된 마지막 탑의 인덱스 + 1 값을 저장하고 반복문 종료
        if stack[-1][1] >= T[i]:
            answer.append(stack[-1][0] + 1)
            break
        # 스택에 저장된 마지막 탐의 높이가 입력받은 탑의 높이보다 작으면 수신할 수 없기 때문에
        # 스택에 저장된 마지막 탑 삭제
        else:
            stack.pop()
    # 스택이 비어있으면 수신할 탑이 당연히 없기 때문에 탑 번호 저장 리스트에 0값 저장
    if not stack:
        answer.append(0)

    # 탑 번호만 저장했으므로 마지막에 스택에 입력받은 탑의 인덱스와 값 저장
    stack.append((i, T[i]))

# 탑 번호가 저장된 리스트값 모두 출력
print(*answer)