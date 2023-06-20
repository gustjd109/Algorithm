# 이 문제를 풀기 위해서는 아래 두 개의 배열이 필요하다.
# 원에 앉아있는 사람들이 저장될 배열과 제거된 사람들을 넣을 배열이 필요하다.
# 그리고, 제거될 사람의 인덱스 번호를 0으로 초기화시켜 준다.
# 이제 사람 수 N 만큼 아래 과정을 반복한다.
# 1. 제거될 사람의 인덱스 번호에 제거되는 순서에서 1을 뺀 값을 더해준다.
#    - 현재 인덱스도 순서에 포함되기 때문이다.
# 2. 만약, 제거될 사람의 인덱스 번호가 원에 앉아있는 사람들의 수보다 같거나 크면, 제거될 사람의 인덱스 번호를 원에 않아있는 사람들의 수로 나눈 나머지로 저장한다.
#    - 원 한바퀴를 돌고, 원의 제일 처음부터 다시 돌 수 있도록 하기 위함이다.
# 3. peoples 배열에서 제거될 사람의 인덱스 번호에 해당하는 사람을 제거하고, 그 사람을 결과 배열에 추가한다.
#    - 사람을 제거할 때 문자열 형식으로 제거시켜 준다.
#    - 리스트를 출력할 때 같이 출력되는 '['와 ']'을 제거하기 위함이다.
#    - '['와 ']'는 replace('[', '<')와 replace(']', '>')를 이용하여 문자를 대체할 수도 있다.
#      - 예 : print(str(result).replace('[', '<').replace(']', '>'))

import sys

sys.stdin = open("input.txt","rt")
N, K = map(int, sys.stdin.readline().split())
peoples = [i for i in range(1, N + 1)]
result = []
remove_idx = 0

for i in range(N):
    remove_idx += (K - 1)
    if remove_idx >= len(peoples):
        remove_idx %= len(peoples)
    result.append(str(peoples.pop(remove_idx)))

print('<', ', '.join(result), '>', sep='')