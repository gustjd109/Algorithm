import sys

def Solve(depth):
    global Answer # 전역변수로 선언한 Answer 변수값을 매개변수로 불러오기 위해 글로벌 변수로 선언(함수에 매개변수로 전달 안해주면 못 불러오는건가?)
    if depth == N: # 탐색한 깊이 변수 값이 입력받은 수의 개수와 같다면
        Sum_Num = 0 # 배열 A에 들어 있는 수들을 모두 더해줄 변수를 0으로 초기화
        for i in range(N - 1): # 배열 A에 들어 있는 수들을 i부터 N - 1번까지 반복문 수행(마지막 수 다음 수는 없기 때문에 N - 1로 설정)
            Sum_Num += abs(N_Arr[i] - N_Arr[i + 1]) # i ~ N - 1번 수까지 i번 수에서 i + 1수를 뺀 절대값을 모두 더함
        Answer = max(Answer, Sum_Num) # 모두 더한 값과 최대값이 저장된 Answer값과 비교하여 더 큰값을 리턴
        return

    for i in range(N): # 0부터 N - 1번 반복문 수행
        if not Visited[i]: # i번째 수가 방문하지 않은 상태이면(같은 값이 중복되는 것을 방지)
            Visited[i] = True # i번쨰 수를 방문 처리
            N_Arr.append(A[i]) # 방문한 수를 임시 배열에 삽입
            Solve(depth + 1) # Slove함수 재귀호출
            Visited[i] = False # 재귀호출 함수가 끝나게되면 i번째 수를 방문하지 않은 상태로 처리
            N_Arr.pop() # 임시 배열에서 i번째 수 삭제

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
N_Arr = []
Visited = [False] * N
Answer = -sys.maxsize # 파이썬에서 최댓괎과 최솟값을 지정하는 방법 중 하나
                      # sys.maxsize는 9223372036854775808값이 들어가며, -sys.maxsize는 -9223372036854775808이 들어감
                      # 다른 방법으로는 Value = float('inf')와 Value = float('-inf')도 있음(sys.maxsize보다 수가 큼)

Solve(0)
print(Answer)

# 해당 문제를 풀기 위해서는 DFS(깊이 우선 탐색) 알고리즘을 알고 있어야 함
# DFS 알고리즘을 알기 위해서는 추가적으로 스택에 대해서도 알고 있어야 함
# 해당 문제를 풀기 위해 N과 M 시리즈 12문제를 풀어보는 것이 좋음
# 해당 12문제가 스택을 이용한 DFS를 연습할 수 있는 문제임
# 추가적으로 10971번 외판원 순회2 문제도 DFS를 이용하여 푸는 문제임