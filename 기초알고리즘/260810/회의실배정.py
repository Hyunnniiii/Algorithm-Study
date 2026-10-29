# 힙으로 풀어보자
from heapq import heappush, heapify, heappop

N = int(input())
hq = []

# 끝나는 시간을 기준으로 정렬
for _ in range(N):
    number, start, end = map(int, input().split())
    heappush(hq, (end, start, number))

# 끝나는 시간이 빠른 순서대로 꺼내기: 이전 end보다 start가 작으면 pass
last_end = 0
lst = []
cnt = 0
while hq:
    e, s, n = heappop(hq)
    if s >= last_end:
        lst.append(n)
        cnt += 1
        last_end = e
print(cnt)
print(*lst)