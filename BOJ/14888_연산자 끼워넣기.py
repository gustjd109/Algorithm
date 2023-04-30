import sys
sys.setrecursionlimit(10**9)

def dfs(i, now_val):
    global add, sub, mul, div, max_val, min_val

    # 인덱스가 N이 되면, 모든 연산을 완료한 것이므로 최대, 최소값 계산
    if i == N:
        max_val = max(max_val, now_val)
        min_val = min(min_val, now_val)

    else:
        # 더하기 연자가 1개 이상이면
        if add > 0:
            # 더하기 연산자 1개 사용할 것이므로 더하기 연산자 -1
            add -= 1
            # 다음 연산할 인덱스와 연산된 결과값 전달
            dfs(i + 1, now_val + array[i])
            # 연산이 완료되었으면 다시 연산자의 개수 +1
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now_val - array[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now_val * array[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now_val / array[i]))
            div += 1

if __name__ == "__main__":
    # 초기 최대, 최소값 설정
    max_val, min_val = -sys.maxsize, sys.maxsize
    # 수의 개수 입력
    N = int(sys.stdin.readline())
    # 수열 입력
    array = list(map(int, sys.stdin.readline().split()))
    # 연산자 수 입력
    add, sub, mul, div = map(int, sys.stdin.readline().split())

    dfs(1, array[0])

    print(max_val)
    print(min_val)