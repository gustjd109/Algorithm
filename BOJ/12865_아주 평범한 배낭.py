import sys

def DP(N, K):
    # 각 물품을 탐색하고, 1 ~ 최대무게를 탐색
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            # 현재 물건이 해당열의 무게보다 작거나 같으면, 
            # 현재 물건을 담을 수 있으므로 물건을 담았을 때와 담지 않았을 때의 가치를 비교해준 뒤 더 큰 값을 할당
            if j >= items[i][0]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i][0]] + items[i][1])
            # 현재 물건이 해당열의 무게보다 크면, 
            # 현재 물건을 담을 수 없으므로 이전 물건의 현재 무게의 값을 할당
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 물품의 수 N과 준서가 버틸 수 있는 무게 K 입력
    N, K = map(int, sys.stdin.readline().split())
    # 각 물건의 무게 W와 가치 V를 N개 만큼 입력
    items = [[0, 0]]
    for i in range(1, N + 1):
        items.append(list(map(int, sys.stdin.readline().split())))
    # DP테이블 생성 : i, j가 1이상일 때부터 검사할 수 있도록 편의상 i, j가 0일때는 모두 0을 넣어 마진값 설정
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    print(DP(N, K))