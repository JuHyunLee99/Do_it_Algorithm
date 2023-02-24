# 백준 11659 구간 합 구하기1

import sys
input = sys.stdin.readline

# 합 배열
# S[i] = A[0] + A[1] + A[2] + ... + A[i-1] + A[i]   # A[0]부터 A[i] 까지의 합
# S[i] = S[i-1] + A[i]

# 구간 합 구하는 공식
# S[j] - S[i-1]  # i에서 j까지의 합



n, m = map(int, input().split())    # n(숫자 개수), m(질의 개수) 입력
mylist = list(map(int, input().split()))    # 배열 리스트 입력    
prefix_sum = [0]    # 합 배열 리스트 선언
temp = 0    # 변수 선언

# 합 배열 만들기
for i in mylist:
    temp = temp + i
    prefix_sum.append(temp)

# 합 배열에서 구간 합 구하기
for _ in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])