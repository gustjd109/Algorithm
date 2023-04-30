import sys

S = sys.stdin.readline().strip()

# 입력받은 문자열 S가 P 또는 PPAP인 경우, PPAP문자열로 판단하여 'PPAP' 출력
if S == 'P' or S == 'PPAP':
    print('PPAP')
# 입력받은 문자열 S가 P 또는 PPAP 둘 다 아닌 경우
else:
    stack = []
    PPAP = ['P', 'P', 'A', 'P']
    # 문자열 S의 각 원소 탐색
    for i in S:
        # 스택에 문자열 S의 i원소 삽입
        stack.append(i)
        # 만약 스택에 저장된 마지막 값부터 -4번째 값까지 PPAP 문자열이 존재하면
        if stack[-4:] == PPAP:
            # 스택에서 P를 제외한 3개 원소인 'P', 'A', 'P' 삭제
            stack.pop()
            stack.pop()
            stack.pop()

    # 문자열 S의 모든 원소의 탐색을 끝낸 후, 
    # 스택에 남은 값이 'P' 또는 'PPAP'이면 'PPAP' 출력하고, 아니면 'NP' 출력
    if stack == ['P'] or stack == PPAP:
        print('PPAP')
    else:
        print('NP')

# 이 문제는 입력받은 문자열이 'P' 또는 'PPAP'이면 PPAP문자열로 판단하여 'PPAP'를 출력하고,
# 아니면 아래 과정을 반복하여 결과값을 얻는다.
# 입력받은 문자열의 각 원소를 탐색하면서 스택에 원소를 하나씩 삽입시킨다.
# 삽입한 후, 스택에 저장된 마지막 값부터 -4번째 값까지 검색하여 'PPAP' 문자열이 존재하면
# 스택에서 제일 앞의 'P'를 제외한 나머지 문자열인 'PAP'를 삭제한다.
# 이렇게 하면, 'PPAP'문자열을 'P'로 변환한 것과 같은 효과를 볼 수 있다.
# 문자열의 모든 원소에 대해 탐색이 종료되면, 스택에 남은 값을 확인하다.
# 확인했을 때, 'P' 또는 'PPAP'가 남아있으면 'PPAP'를 출력하고, 아니면 'NP'를 출력한다.