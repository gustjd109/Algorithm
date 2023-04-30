# deque를 이용한 풀이
from collections import deque
import sys

N = int(sys.stdin.readline())
Q = deque([i for i in range(1, N + 1)])

while len(Q) > 1:
    Q.popleft()
    Q.rotate(-1)

print(Q[0])

# 분명 큐의 원소들을 양방향으로 로테이션하는 기능이 있을거라고 생각
# 역시나 rotate 함수가 있음(개꿀)
# 큐.rotate(1) -> 오른쪽으로 이동
# 큐.rotate(-1) -> 왼쪽으로 이동

#############################################################################

# 규칙을 이용한 풀이
import sys

N = int(sys.stdin.readline())
tmp = 1
while N > tmp:
    tmp *= 2
print(2 * N - tmp)

# 규칙을 찾아보면
# N = 1 -> 1
# N = 2 -> 2 * 2 - 2
# N = 3 -> 2 * 3 - 4
# N = 4 -> 2 * 4 - 4
# N = 5 -> 2 * 5 - 8
# N = 6 -> 2 * 6 - 8
# 순으로 나오며, (2 * N) - M라는 식이 나온다.
# 이때, M은 1부터 시작해서 N > M가 아닐때까지 2를 누적해서 곱하여 구할 수 있다.