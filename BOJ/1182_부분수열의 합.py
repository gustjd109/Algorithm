import sys

def solve(start):
    global cnt
    if sum(Tmp_Arr) == S and len(Tmp_Arr) > 0: # len(Tmp_Arr) > 0 : 부분수열 조건으로 아무것도 선택하지 않은 경우를 제외
        cnt += 1
    
    for i in range(start, N):
        Tmp_Arr.append(N_List[i])
        solve(i + 1) # 중복을 허용하지 않기 위해 인덱스에 i + 1을 전달
        Tmp_Arr.pop()

N, S = map(int, sys.stdin.readline().split())
N_List = list(map(int, sys.stdin.readline().split()))
Tmp_Arr = []
cnt = 0
solve(0)
print(cnt)

# DFS와 재귀함수를 이용한 풀이
# 해당 문제를 풀기위해 부분수열이라는 것이 무엇인지 확인해보자
# 부분수열이란 해당 수열에 있는 수들의 모든 조합을 말한다.
# 예를 들어, [1, 2, 1, 3, 5, 6] 수열이 있다고 하자
# [2, 1, 3]처럼 수들이 연속된 경우 뿐만 아니라, [1, 1, 3] 처럼 불연속적으로 선택된 수들도 부분 수열이다.
# 다만, 아무것도 선택하지 않은 경우 ([])는 제외된다.
# 즉, 이 문제는 중복을 허용하지 않고 원소를 더한 값이 S가 되는 모든 경우의 수를 구하는 문제이다.

# 추가 내용
# UnboundLocalError: cannot access local variable 'cnt' where it is not associated with a value
# 해당 에러는 파이썬에서 전역 변수의 데이터를 확인할 수는 있지만, 수정할 수는 없기 떄문에 전역 변수를 수정하고 싶은 경우 global로 정의를 해줘야 한다.