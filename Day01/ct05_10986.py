# 백준 10986 나머지 합 구하지

import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # n(숫자 개수), m(나누어떨어져야 하는 수)
A = list(map(int, input().split())) # 원본 리스트
S = [0] * n # 합 배열
C = [0] * m # 같은 나머지의 인덱스를 카운트하는 리스트
S[0] = A[0] 
answer = 0  # 정답 변수

# 합 배열 구하기
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# 합 배열을 M으로 나눈 나머지 값
for i in range(n):
    remainder = S[i] % m    # 합 배열의 모든 값에 % 연산 수행
    if remainder == 0:      # 0~i까지의 구간 합이 m으로 나누어 떨어질때
        answer += 1         # 정답에 +1
    C[remainder] += 1       # 나머지 같은 인덱스 카운트

# 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기(조합C[i]C2)
for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)

print(answer)