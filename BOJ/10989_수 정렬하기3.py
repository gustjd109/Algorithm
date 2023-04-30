import sys

N = int(sys.stdin.readline())
NumArr = [0] * 10001

for i in range(0, N):
    Num = int(sys.stdin.readline())
    NumArr[Num] += 1

for i in range(0, 10001):
    if NumArr[i] != 0:
        for j in range(0, NumArr[i]):
            print(i)

# 이 문제는 기존에 풀던 방식으로 풀 경우 시간초과와 메모리 초과이 발생한다.
# 메모리 초과 해결 방법 : 파이썬 내장 함수인 sort() 함수 사용 시, append할 때마다 메모리가 쌓이기 때문에 계수정렬을 사용해야 한다.
# 시간 초과 해결 방법 : input() 대신 sts.stdin.eadline()을 사용하여 수행 시간을 많이 줄일 수 있다.
# 이 문제는 수의 개수가 10,000,000개 까지 주어질 수 있지만, 
# 입력에는 10,000개보다 작거나 같은 자연수가 주어진다고 나와있다.
# 즉, 수가 중복될 수 있다는 것이다.
# 이때 사용하는 정렬방법이 계수정렬이다.
# 계수정렬은 입력값 범위 만큼 배열을 하나 만들어주어 입력받을 때마다 그 수에 해당하는 배열 인덱스에 +1을 해주어 저장한다.
# 입력값을 모두 받은 후, 다시 배열을 돌면서 값이 0이 아니라면 값만큼 인덱스에 해당하는 숫자를 출력해준다.

# 참고 사이트 : https://coarmok.tistory.com/entry/파이썬python-백준-10989번-메모리-초과