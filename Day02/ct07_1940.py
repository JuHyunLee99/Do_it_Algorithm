# 백준 1940 주몽의 명령
import sys
input = sys.stdin.readline

n = int(input())    # 재료의 개수
m = int(input())    # 갑옷이 되는 번호
A = list(map(int, input().split()))  # 재료 데이터 저장 리스트
A.sort()    # 투포인터 원칙을 사용하여 크기 비교를 위해 리스트 정렬
i, j = 0, n-1
count = 0   # 만들 수 있는 갑옷의 수

while i < j:
    if A[i] + A[j] < m:
        i += 1
    elif A[i] + A[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)


