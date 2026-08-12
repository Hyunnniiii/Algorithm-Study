for TC in range(1, int(input())+1):
    N, E = map(int, input().split())    # 노드의 개수 N, 간선 정보의 개수 E

    # 인접리스트
    adj = [[] for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s]. append([e, w])

    # D: 거리 표시할 리스트. 초기에 거리 무한으로 설정
    distance = [float('inf')]*N


    from heapq import heappush, heapify, heappop

    def dijkstra(start):
        q = []      # 노드 정보들 넣어둘 큐
        heappush(q, (0, start))     # (거리, 노드번호) 형태로 리스트에 추가
        distance[start] = 0

        while q:
            # 우선순위가 가장 낮은 값 = 가장 짧은 거리 불러오기
            dist, now = heappop(q)

            # 이미 입력되어있는 값이 현재까지의 거리보다 짧으면 > 갱신 X
            if distance[now] < dist:
                continue

            # adj 리스트에 있는, 현재 노드(now)와 연결된 노드를 탐색
            for nxt, ni in adj[now]:
                # 기존에 입력된 값보다 계산한 거리가 짧으면 갱신
                # 좌: 현재 노드까지의 거리(dist) + 그 다음(nxt)까지 가는 거리(nxt[1])
                # 우: 현재 입력되어 있는 거리
                if dist + nxt[1] < distance[nxt[0]]:
                    # 최단거리로 바꿔주고, 큐에 넣어준다
                    distance[nxt[0]] = dist + nxt[1]
                    heappush(q, [dist + nxt[1], nxt[0]])

    dijkstra(0)
    print(f'#{TC} {distance[N-1]}')

# ===================
import heapq

def dijk(sw, si):
    hq = []
    heappush(hq, (sw, si))

    while hq:
        # 현재 hq에서 가장 비용이 작은 경로 불러오기
        now, ci = heappop(hq)   # now: 거리, ci: 현재 노드 번호

        # 현재 저장된 거리가 더 짧으면 갱신할 필요 없음
        if dst[ci] < now:
            continue

        # 그렇지 않으면 최단 경로로 저장
        dst[ci] = now

        # 현재 노드와 인접한 노드들 중에
        for nxt, ni in adj[ci]:
            # 현재 저장된 거리보다 더 짧은 경로를 hq에 추가
            if dst[ni] > now + nxt:
                heapq.heappush(hq, (now + nxt, ni))

T = int(input())
for tc in range(1, T + 1):
    # [입력] 노드 N개, (출발, 도착, 비용) E개
    N, E = map(int, input().strip().split())

    # 인접 리스트 저장.
    adj = [[] for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().strip().split())
        adj[s].append((w, e))

    dst = [float('inf')] * N
    dijk(0, 0)

    # [출력] 마지막 노드의 최단 경로 값
    print(f'#{tc} {dst[N - 1]}')

# ====================
