# k < n : k번째 제거, 총 n명
# 마지막으로 제외되는 사람 구하기
n, k = map(int, input().split())

people = []
for i in range(1, n+1):
    people.append(i)    # 사람 큐
seq = []    # 제외되는 사람 순서
idx = 1

while people:
    if idx % k != 0:
        a = people.pop(0)
        people.append(a)
    else:
        a = people.pop(0)
        seq.append(a)
    idx += 1

print(*seq)
