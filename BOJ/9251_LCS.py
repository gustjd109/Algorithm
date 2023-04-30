import sys

def LCS(str_a, str_b):
	# 두 문자열을 한글자씩 비교
	for i in range(1, len(str_a) + 1):
		for j in range(1, len(str_b) + 1):
			# 두 문자가 같다면 dp[i - 1][j - 1]값을 찾아 1증가
			if str_a[i - 1] == str_b[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + 1
			# 두 문자가 다르다면 dp[i - 1][j]와 dp[i][j - 1]중에서 큰값을 표시
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
	# dp테이블의 마지막 값 출력
	return dp[-1][-1]

if __name__ == "__main__":
	sys.stdin = open("input.txt","rt")
	# 두 문자열 입력
	str_a = sys.stdin.readline().strip()
	str_b = sys.stdin.readline().strip()
	# DP테이블 생성 : i, j가 1이상일 때부터 검사할 수 있도록 편의상 i, j가 0일때는 모두 0을 넣어 마진값 설정
	dp = [[0] * (len(str_b) + 1) for _ in range(len(str_a) + 1)]
	# 두 문자열에 대한 최장 공통 부분수열 출력
	print(LCS(str_a, str_b))