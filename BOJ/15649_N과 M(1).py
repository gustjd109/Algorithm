import sys

def DFS():
    if len(S) == M: # 만약, 방문 리스트의 길이가 출력할 수의 길이인 M과 같다면,
        print(*S) # 방문 리스트를 unpacking하여 출력(리스트 뒤에 *를 입력하면, 리스트를 unpacking한다는 의미로 *[1, 2, 3] = 1, 2, 3이 출력)
        return # 방문 리스트를 출력 후 리턴
    
    for i in range(1, N + 1): # N번 만큼 반복문 실행
        if visited[i]: # 만약 i번 숫자가 방문했다면, 건너뜀(같은 숫자 중복 방지를 위해)
            continue

        visited[i] = True # 만약 i번 숫자가 방문하지 않았다면, i번 째 방문 체크 리스트 값을 True로 변경
        S.append(i) # i번 숫자가 방문했으므로 방문한 숫자를 저장할 리스트에 삽입
        DFS() # 함수 다시 호출
        S.pop() # 방문 리스트를 unpacking하여 출련한 후, 제일 마지막 숫자를 삭제
        visited[i] = False # 방문 체크 리스트 값을 False로 변경

N, M = map(int, sys.stdin.readline().split()) # N, M 입력
S = [] # 방문한 숫자를 저장할 리스트
visited = [False] * (N + 1) # 방문 체크를 위한 리스트로 숫자 N개 만큼 False로 초기화
DFS() # 함수 호출

# 스택을 이용하여 문제를 푸신 분의 코드
# import sys

# def DFS():
#     if len(s) == M:
#         print(*s)
#         return

#     for i in range(1, N+1):
#         if i in s:
#             continue

#         s.append(i)
#         DFS()
#         s.pop()
        
# N, M = map(int, sys.stdin.readline().split())
# s = []
# DFS()