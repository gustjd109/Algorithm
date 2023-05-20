# 반복문을 이용한 풀이
# python3는 시간초과가 발생하며, pypy3로 하면 통과된다.
import sys

sys.stdin = open("input.txt","rt")
n = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
result = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if num_list[i] + num_list[j] == x:
            result += 1
        if num_list[i] + num_list[j] > x:
            break
print(result)

# 투 포인터를 이용한 풀이
# start 값이 end값 보다 클때까지 while문을 반복한다.
# 이때 num_list에서 start와 end 인덱스 값을 더한 값이 x값과 같다면, 결과값과 start값을 1 증가시켜 준다.
# 만약 num_list에서 start와 end 인덱스 값을 더한 값이 x값 보다 크다면, end값을 1 감소시켜 준다.
# 위 두 조건에 만족하지 않으면, num_list에서 start와 end 인덱스 값을 더한 값이 x값 보다 작은 경우이므로 start값만 1 증가시켜 준다.
# start 값이 end값 보다 크면, 반복문을 빠져나와 결과값을 출력해준다.
import sys

sys.stdin = open("input.txt","rt")
n = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

result = 0
start = 0
end = n - 1

while start < end:
    num_sum = num_list[start] + num_list[end]
    if num_sum == x:
        result += 1
        start += 1
    elif num_sum > x:
        end -= 1
    else:
        start += 1

print(result)