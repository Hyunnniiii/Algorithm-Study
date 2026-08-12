# 현재 만드는 소시지의 길이와 너비가 바로 이전의 소시지의 길이/너비보다 크거나 같아야 작동
# 만약 작다면 준비 작업 1분 소요 / 첫 소시지 만들 때 준비 1분 소요
# 구할 것: ''준비 작업''에 소요한 최소 시간
from heapq import heappush, heapify, heappop
N = int(input().strip())
# 길이 기준 / 너비 기준일 때 각각 구해서 준비작업 작은 것을 선택?
length_q = []
area_q = []

# 길이 / 너비 기준 힙큐 각각 생성
lst = list(map(int, input().split()))
for _ in range(N):
    sl, sw = lst[0], lst[1]
    del lst[0:2]

    heappush(length_q, (sl, sw))
    heappush(area_q, (sw, sl))

# 길이 기준일 때 소요 시간 구하기
l_time = 1
length1, area1 = heappop(length_q)
while len(length_q) >= 1:
    length2, area2 = heappop(length_q)

    if area1 > area2:
        l_time += 1
    length1, area1 = length2, area2

print(l_time)

# 너비 기준일 때 소요 시간 구하기
a_time = 1
area1, length1 = heappop(area_q)
while len(area_q) >= 1:
    area2, length2 = heappop(area_q)

    if length1 > length2:
        a_time += 1
    area1, length1 = area2, length2
print(a_time)

# 최소 시간 출력
print(min(l_time, a_time))

# =============== 아님

# 정렬해서 제일 앞 소시지 고르고, 기계 안바꾸고 만들 수 있을 만큼 전부 만든다

