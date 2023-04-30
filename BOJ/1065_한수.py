def FindHansu(N):
    HansuCnt = 0
    for i in range(1, N + 1):
        N_List = list(map(int, str(i)))
        if i < 100:
            HansuCnt += 1
        elif N_List[0] - N_List[1] == N_List[1] - N_List[2]:
            HansuCnt += 1
    return HansuCnt

N = int(input())
print(FindHansu(N))

# 한수 : 각 수의 자리가 등차수열을 이루는 수
# 등차수열 : 숫자와 숫자 사이의 간격이 동일한 숫자의 나열
# 두자리 숫자는 등차수열인지 비교 대상이 없기 때문에 모두 한수(1 ~ 99)이며, 
# 그 이상의 숫자는 각 자리의 숫자 간격이 동일하면 한수임
# 숫자와 숫자 사이의 간격을 확인하기 위해서는 각 자리의 숫자를 확인할 수 있어야 함
# 한수인지 확인하기 위한 숫자를 정수 타입에서 리스트 타입으로 변환 필요
# 각 자릿수를 분리하고 각 자릿수를 비교하기 위해 다시 정수 타입으로 변환 필요