import sys

# 행렬 곱 함수
def matrix_mul(matrix_a, matrix_b):
    length = len(matrix_a)
    tmp = [[0] * length for _ in range(length)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += matrix_a[i][k] * matrix_b[k][j]
                # 행렬의 각 성분의 숫자들은 1000이 넘어가면 1000으로 나눠줘야 함
                tmp[i][j] %= 1000
    return tmp

# 행렬 제곱 함수
def matrix_pow(matrix_a, M):
    if M == 1:
        return matrix_a
    if M % 2 == 0:
        tmp = matrix_pow(matrix_a, M // 2)
        return matrix_mul(tmp, tmp)
    else:
        tmp = matrix_pow(matrix_a, M - 1)
        return matrix_mul(tmp, matrix_a)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    result = matrix_pow(matrix_a, M)

    for i in range(N):
        print(' '.join(map(str, result[i])))