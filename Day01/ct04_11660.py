# 백준 11660 구간합 구하기2

import sys
input = sys.stdin.readline

# 2차원 합 배열
# D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 2차원 구간 합 공식
# (x1,y1)에서 (x2, y2)까지의 합
# D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]


# 행렬은 (1,1)부터 시작하는데 리스트 인덱스는 0부터 시작.
# 그러므로 행렬 크기를 n+1로 하여 인덱스 [0]구간은 안씀.
n, m = map(int, input().split())    # n(숫자 개수), m(질의 개수) 입력
A = [[0]* (n+1)]    # 원본 리스트
D = [[0] * (n+1) for _ in range(n+1)]   # 합 배열
# D = [[0 for _ in range(n+1)] for _ in range(n+1)] # 2차원 리스트 표현식2

# 원본 리스트 데이트 저장
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
    # print(A_row)
# print(A)

# 합 배열 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
# print(D)

# 합 배열에서 구간 합 구하기
for _ in range(m):
    x1, y1, x2, y2 =  map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)

