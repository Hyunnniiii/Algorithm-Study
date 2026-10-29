# 합이 최소인 것들을 선택해서 더한다
# 최소인거 2개 선택해서 더하면 될듯?
# 정렬해서 앞에서부터 2개 더하고, 또 정렬하고,,
from heapq import heappush, heapify, heappop

N = int(input())
lst = list(map(int, input().split()))
heapify(lst)

# 작은거 2개 더해서, 다시 추가 > 숫자 1개만 남을 때까지
sum = 0
while len(lst) > 1:
    one = heappop(lst)
    two = heappop(lst)
    a = one + two
    sum += a
    heappush(lst, a)
print(sum)

