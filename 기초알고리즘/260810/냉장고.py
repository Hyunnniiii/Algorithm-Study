# 빨리 끝나는거 기준으로 겹치는거 다 빼버리기??
from heapq import heappush, heapify, heappop

N = int(input().strip())
temp = []

for _ in range(N):
    start, end = map(int, input().split())
    heappush(temp, (end, start))

e, s = heappop(temp)
cnt = 1     # 첫 번째 구간 냉장고

while temp:
    e1, s1 = heappop(temp)

    # 현재 냉장고 온도와 겹치는 부분 있으면 계속 진행
    if s1 <= e:
        continue

    # 온도 겹치지 않으면 새 냉장고
    else:
        e = e1
        cnt += 1

print(cnt)
