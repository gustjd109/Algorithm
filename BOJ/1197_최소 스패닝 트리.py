import sys

# Union 연산 수행1 : 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union 연산 수행2 : 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    # 정점의 개수 v과 간선의 개수 e 입력
    v, e = map(int, sys.stdin.readline().split())
    # Union 연산 준비 1단계 : 부모 테이블 초기화
    parent = [0] * (v + 1)

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    result = 0

    # Union 연산 준비 2단계 : 부모 테이블상에서 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    # 모든 간선과 기중치에 대한 정보 입력
    for i in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        # 가중치순으로 정렬하기 위해서 튜플의 첫 번째 원소를 가중치로 설정
        edges.append((c, a, b))

    # 간선을 가중치순으로 정렬
    edges.sort()

    # 간선을 하나씩 확인하며
    for edge in edges:
        c, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            # Union 연산 수행
            union_parent(parent, a, b)
            result += c

    print(result)