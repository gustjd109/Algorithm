import sys
from collections import deque

while True:
    rec = list(map(int, sys.stdin.readline().split()))
    # 직사각형 높이가 저장된 rec리스트의 0번 째 값은 직사각형 N개의 수로 pop하여 따로 저장
    n = rec.pop(0)

    # 문제 조건에 의해 직사각형의 개수가 0이면 종료
    if n == 0:
        break

    # 직사각형 높이가 저장된 rec리스트에서 하나씩 꺼내와서 넓이 계산을 하기 위한 스택
    stack = deque()
    answer = 0

    # 왼쪽 직사각형의 높이부터 차례대로 탐색
    for i in range(n):
        # 스택이 비어있지 않고, rec 리스트에서 스택에 저장된 마지막 값인 인덱스값이 rec[i]값보다 크면
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            # 스택에서 데이터를 삭제하고, 삭제한 값을 임시 변수에 저장
            tmp = stack.pop()

            # 스택이 비어있으면, 길이 값에 i 삽입
            if len(stack) == 0:
                width = i
            # 스택이 비어있지 않으면, 길이 값에 (i - 스택의 마지막 값 - 1) 삽입
            else:
                width = i - stack[-1] - 1
            # 구해진 길이 값으로 넓이를 구한 후, 이전 최대 넓이 값과 비교하여 더 큰 값을 결과값 저장 변수에 삽입
            answer = max(answer, width * rec[tmp])
        # 스택이 비어있으면 i값 삽입
        stack.append(i)

    # 모든 직사각형의 높이를 탐색 완료했지만, 아직 스택이 비어있지 않으면
    while len(stack) != 0:
        # 스택에서 데이터를 삭제하고, 삭제한 값을 임시 변수에 저장
        tmp = stack.pop()

        # 스택이 비어있으면, 길이 값에 직사각형 개수인 n값 삽입
        if len(stack) == 0:
            width = n
        # 스택이 비어있지 않으면, 길이 값에 (직사각형의 개수인 n - 스택의 마지막 값 - 1) 삽입
        else:
            width = n - stack[-1] - 1
        # 구해진 길이 값으로 넓이를 구한 후, 이전 최대 넓이 값과 비교하여 더 큰 값을 결과값 저장 변수에 삽입
        answer = max(answer, width * rec[tmp])

    # 결과값 출력
    print(answer)