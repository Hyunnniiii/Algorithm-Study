N = int(input().strip())    # 학원의 수
mat = [list(map(int, input().split())) for _ in range(N)]

lst = []    # 출발, 도착, 거리 저장할 리스트
parent = [i for i in range(N+1)]    # 0 주의
for x in range(N):
    for y in range(N):
        if x >= y:
            lst.append((x+1, y+1, mat[x][y]))
# 거리 짧은 순서대로 정렬
lst.sort(key = lambda x: x[2])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    parent[a] = b

# 거리 제일 짧은거 우선으로 고르면서
# 그 다음에 고른 경로가 사이클 만들면 패스
min_cost = 0
for start, end, weight in lst:
    # 이미 고른 거면 패스
    if find(start) == find(end):
        continue
    # 아니면 추가
    min_cost += weight
    union(start, end)

print(min_cost)