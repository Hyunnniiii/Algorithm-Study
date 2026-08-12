from heapq import heappush, heapify, heappop
N = int(input())
alst = list(map(int, input().split()))  # 처음에 가지고 있는 돈
heapify(alst)
M = int(input())

# 제일 적은 사람이 돈 가지고, 정렬하기 반복
money = list(map(int, input().split()))

for money in money:

    # 제일 돈이 없는 사람에게 돈 지급
    a = heappop(alst)
    heappush(alst, a + money)

# 오름차순 출력하기
while alst:
    n = heappop(alst)
    print(n, end=' ')