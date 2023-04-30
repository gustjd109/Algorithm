# 트리를 사용한 풀이
import sys
# 재귀 최대 깊이 설정
sys.setrecursionlimit(10**9)

# 전위 순회한 결과를 이진 검색 트리로 만들어주는 함수
def maketree(N_list):
    # 전위 순회 입력값 리스트의 길이가 0이면, 리턴
    if len(N_list) == 0:
        return
    
    # 왼쪽, 오른쪽 서브트리 초기화
    left_subtree = []
    right_subtree = []
    # 루트값을 전위 순회 입력값 리스트의 0번째 인덱스 값으로 설정
    root = N_list[0]
    # 루트값을 이미 저장했기 때문에 전위 순회 입력값 리스트의 두 번째 인덱스부터 전위 순회 입력값 리스트의 마지막 인덱스까지 반복문 수행
    for i in range(1, len(N_list)):
        # 전위 순회 입력값 리스트의 i번째 값이 루트값보다 작으면, 왼쪽 서브트리에 i번째 값 삽입
        if N_list[i] < root:
            left_subtree.append(N_list[i])
        # 전위 순회 입력값 리스트의 i번째 값이 루트값보다 크면, 오른쪽 서브트리에 삽입
        else:
            right_subtree.append(N_list[i])
    # 반복문 종료

    # 왼쪽과 오른쪽 두 서브트리의 길이가 0이 아니면, 
    # 트리의 루트값(키)에 연결되는 왼쪽 노드에 왼쪽 서브트리의 0번째 값을
    # 오른쪽 노드에는 오른쪽 서브트리의 0번째 값을 삽입
    if len(left_subtree) != 0 and len(right_subtree) != 0:
        tree[root] = [left_subtree[0], right_subtree[0]]
    # 왼쪽 서브트리의 길이가 0이 아니고 오른쪽 서브트리의 길이가 0이면, 
    # 트리의 루트값(키)에 연결되는 왼쪽 노드에 왼쪽 서브트리의 0번째 값을
    # 오른쪽 노드에는 '.'을 삽입
    elif len(left_subtree) != 0 and len(right_subtree) == 0:
        tree[root] = [left_subtree[0], "."]
    # 왼쪽 서브트리의 길이가 0이고 오른쪽 서브트리의 길이가 0이 아니면,
    # 트리의 루트값(키)에 연결되는 오른쪽 노드에는 '.'을 
    # 왼쪽 노드에 왼쪽 서브트리의 0번째 값을 삽입
    elif len(left_subtree) == 0 and len(right_subtree) != 0:
        tree[root] = [".", right_subtree[0]]
    # 왼쪽과 오른쪽 두 서브트리의 길이가 0이면, 리턴
    else:
        return
    
    # 재귀함수를 호출하여 왼쪽, 오른쪽 서브트리의 첫 번째 값을 트리의 루트값으로 하여 반복 수행
    maketree(left_subtree)
    maketree(right_subtree)

# 만들어진 이진 검색 트리로 후위 순회한 결과를 구해주는 함수
def postorder(root):
    # 루트값이 '.'이면, 리턴
    if root == ".":
        return
    # 트리에 루트값이 없으면, 왼쪽과 오른쪽 노드가 없기 때문에 루트값 출력
    if root not in tree:
        print(root)
        return
    # 후위 순회를 하면서 루트값 출력
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root)

if __name__ == "__main__":
    # 전위 순회 입력값 저장 리스트 / 트리 / 입력값의 개수(노드의 개수) 초기화
    N_list = []
    tree = {}
    input_cnt = 0
    # 전위 순회 입력값의 개수(노드의 개수)가 10,000개 이하일때만 반복문 수행
    while input_cnt <= 10000:
        try:
            N_list.append(int(sys.stdin.readline()))
        # 전위 순회 입력값이 10,000개가 넘어가거나, 공백을 입력하면 반복문 종료
        except:
            break
        input_cnt += 1
    
    # 전위 순회한 결과를 이진 검색 트리로 만들어주는 함수 실행
    maketree(N_list)
    # 만들어진 이진 검색 트리로 후위 순회한 결과를 구해주는 함수
    postorder(N_list[0])

#################################################################################################################

# 트리를 사용하지 않고 재귀함수만을 이용한 풀이
import sys
sys.setrecursionlimit(10**9)

# 후위 순회한 결과를 구해주는 함수
def postorder(start, end):
    # 배열을 모두 돌면, 리턴
    if start >= end:
        return
    # mid값을 기준으로 왼쪽, 오른쪽 서브트리로 분할
    mid = end + 1

    for i in range(start + 1, end + 1):
        # 현재 노드보다 큰 i번째 값이 있다면, 그 전까지의 값은 모두 왼쪽 서브트리
        # 현재 노드보다 큰 i번째 값 이후의 값은 모두 오른쪽 서브트리
        if N_list[start] < N_list[i]:
            mid = i
            break

    # 왼쪽 서브트리 재귀함수
    postorder(start + 1, mid - 1)
    # 오른쪽 서브트리 재귀함수
    postorder(mid, end)
    # 후위순회이므로 제일 마지막에 출력
    print(N_list[start])

if __name__ == "__main__":
    # 전위 순회 입력값 저장 리스트 / 트리 / 입력값의 개수(노드의 개수) 초기화
    N_list = []
    input_cnt = 0
    # 전위 순회 입력값의 개수(노드의 개수)가 10,000개 이하일때만 반복문 수행
    while input_cnt <= 10000:
        try:
            N_list.append(int(sys.stdin.readline()))
        # 전위 순회 입력값이 10,000개가 넘어가거나, 공백을 입력하면 반복문 종료
        except:
            break
        input_cnt += 1

# 후위 순회한 결과를 구해주는 함수에 start : 0 / end : 전위 순회 입력값 저장 리스트 길이 - 1값 전달
postorder(0, len(N_list) - 1)