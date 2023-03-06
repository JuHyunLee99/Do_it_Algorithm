# 백준 1253 '좋은 수' 구하기
import sys
input = sys.stdin.readline

N = int(input())    # 데이터 개수
A = list(map(int, input().split()))  # 데이터 리스트
A.sort()
Result = 0  # 좋은 수 개수

for k in range(N):
    find = A[k]
    i, j = 0, N-1
    while i < j:
        if A[i] + A[j] == find:
                if i != k and j != k:
                    Result += 1
                    break
                elif i == k:
                     i += 1
                elif j == k:
                     j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(Result)


