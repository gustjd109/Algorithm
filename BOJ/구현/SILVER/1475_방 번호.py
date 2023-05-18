# 이 문제는 9와 6이 서로 뒤집을 수 있다는 것이라는 조건만 잘 해결해주면 된다.
# 6 또는 9가 나오면, 두 수의 개수가 저장된 리스트에서 둘 중에서 더 작은 개수를 가진 수의 인덱스 값을 증가시켜주면 된다.
# 그 외의 숫자들은 숫자의 개수만큼 인덱스 값을 증가시켜주면 된다.
# 마지막으로, 수의 개수를 저장하는 리스트의 최대값을 출력하면 된다.
import sys

sys.stdin = open("input.txt","rt")
N = input() # sys.stdin.readline()으로 하면, 런타임 에러 발생
N_cnt = [0] * 10
for i in range(len(N)):
    num = int(N[i])
    if num == 6 or num == 9:
        if N_cnt[6] <= N_cnt[9]:
            N_cnt[6] += 1
        else:
            N_cnt[9] += 1
    else:
        N_cnt[num] += 1
print(max(N_cnt))