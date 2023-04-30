import sys

def cutPaper(x, y, N):
    global wcCnt, bcCnt
    # 첫 번째 나오는 색을 초기 색으로 저장
    color = paper[x][y]

    # 색종이를 돌면서 전체 색이 같은지 확인
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 첫 번째 색과 현재 위치의 색이 다르면 색종이를 4분할로 나눠 cutPaper함수를 재귀호출
            if color != paper[i][j]:
                cutPaper(x, y, N // 2) # 1사분면
                cutPaper(x, y + N // 2, N // 2) # 2사분면
                cutPaper(x + N // 2, y, N // 2) # 3사분면
                cutPaper(x + N // 2, y + N //2, N // 2) # 4사분면
                return
    
    if color == 0:
        wcCnt += 1
    else:
        bcCnt += 1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    paper = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
    wcCnt, bcCnt = 0, 0
    cutPaper(0, 0, N)
    print(wcCnt, bcCnt, sep="\n")

# 이 문제는 분할 정복법과 퀴드 트리를 이용하여 해결해야 하는 문제로, 
# 작게 분할한 색종이 안에서 같은 색인지를 판단해 같지 않다면 다시 나누는 과정을 반복한다.
# 쿼드 트리 : 트리의 자식 노드가 4개씩 분할하는 방법