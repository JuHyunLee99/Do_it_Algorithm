# 백준 2018 연속된 자연수의 합 구하기
n = int(input())
count = 1   # 경우의 수, n만 뽑는 경우의 수를 미리 고려하여 초기화
start_index, end_index = 1, 1
sum = 1

while end_index != n:
    if sum == n:    # 정답케이스
        count += 1  # 경우의 수 증가
        end_index +1    # end_index 증가
        sum += end_index    # sum 값 변경
    elif sum > n:
        sum -= start_index  # sum 값 변경
        start_index += 1    # start_index 증가
    else:
        end_index += 1  # end_index 증가
        sum += end_index    # sum 값 변경

print(count)
