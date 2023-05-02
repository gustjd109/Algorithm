import sys

def greedy():
    global cnt

    for i in range(K):
        # 1. 멀티탭에 i번째 전기용품이 이미 꽂혀있을 경우 패스
        if elec_equips[i] in multitap:
            continue
        
        # 2. 멀티탭에 빈 구멍이 있을 경우 빈 공간에 전기용품을 꽂음
        if len(multitap) < N:
            multitap.append(elec_equips[i])
            continue

        # 나중에 꽂아야하는 플러그
        priority = []
        # 3. 멀티탭에 빈 공간이 없는 경우
        for j in multitap:
            # 멀티탭에 꽂혀 있는 플러그가 다음에 꽂아야하는 플러그 중에 있는지 확인
            if j in elec_equips[i:]:
                # 다음에 꽂아야하는 플러그의 순서를 인덱스를 통해 확인하고 인덱스의 위치 값을 가져옴
                # 인덱스 값을 다음에 꽂아야하는 플러그 리스트에 추가
                priority.append(elec_equips[i:].index(j))
            else:
                # 멀티탭에 꽂혀 있는 플러그가 다음에 꽂아야하는 플러그중에 없으면 플러그 사용순서의 최대 범위 +1을 인덱스 값에 삽입
                # 인덱스 값인 101을 다음에 꽂아야하는 플러그 리스트에 추가하여 플러그를 최우선으로 선택
                priority.append(101)

        # 나중에 꽂아야하는 플러그 선택
        target = priority.index(max(priority))
        # 멀티탭에서 나중에 꽂아야하는 플러그 삭제
        multitap.remove(multitap[target])
        # 멀티탭에 i번째 전기용품 추가
        multitap.append(elec_equips[i])
        # 카운트 1증가
        cnt += 1
        
    print(cnt)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 멀티탭 구멍의 개수, 전기 용품의 총 사용횟수 입력
    N, K = map(int, sys.stdin.readline().split())
    # 전기용품 사용 순서대로 입력
    elec_equips = list(map(int, sys.stdin.readline().split()))
    # 플러그를 뺀 횟수 0으로 초기화
    cnt = 0
    # 전기용품을 꽂기 위한 멀티탭 리스트 생성
    multitap = []
    greedy()