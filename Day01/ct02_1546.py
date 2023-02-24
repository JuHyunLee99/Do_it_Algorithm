# 백준 1546 평균 구하기

n = int(input())    # 과목수 입력
mytest = list(map(int, input().split()))    # 과목별 점수 입력
max_point = max(mytest) # 성적 중 최대점수
mysum = sum(mytest) # 과목별 점수들의 합
print(mysum * 100 / max_point/n)    # 평균구하기3