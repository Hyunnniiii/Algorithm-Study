from heapq import heappop, heappush, heapify
N = int(input())
lst = list(map(int, input().split()))

max_heap = []

# 1. 일단 맨 뒤에 넣고 부모와 대소비교, 본인이 더 크면 위치 바꾼다
# 이 역할을 하는게 heappush
for x in lst:
    heappush(max_heap, -x)

for y in max_heap:
    print(-y, end=' ')
print()

# 2. 오름차순으로 정렬된 자료 출력 > heappop 이용
heapify(lst)

while lst:
    n = heappop(lst)
    print(n, end=' ')
