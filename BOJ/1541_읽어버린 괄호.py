import sys

def greedy():
    # 식의 최소값을 저장할 변수 0으로 초기화
    result = 0
    # 다음 뺄셈이 나오기 전의 수들을 '+'를 기준으로 나눠준 후에 모두 더해준다.
    for i in expression[0].split('+'):
        result += int(i)
    # 다음 뺄셈이 나온 후의 수들을 '+'를 기준으로 나눠준 후에 모두 빼준다.
    for i in expression[1:]:
        for j in i.split('+'):
            result -= int(j)
    print(result)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 식 입력
    # 이때, 식의 값이 최솟값이 되기 위해서는 뺄셈을 기준으로 식을 나눠야 한다.
    expression = sys.stdin.readline().split('-')
    # 그리디 알고리즘 수행
    greedy()