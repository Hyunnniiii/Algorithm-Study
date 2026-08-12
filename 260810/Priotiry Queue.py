# 출혈량 높을 수록, 그 다음에 나이 높을 수록 먼저 수술
from heapq import heappush, heappop, heapify
heap = []

for _ in range(int(input())):
        information = input().split()
        if len(information) == 1:
            if heap:
                b, a, n = heappop(heap)
                print(n)
        else:
            command, name, age, blood = information[0], information[1], information[2], information[3]
            heappush(heap, (-float(blood), -float(age), name))

