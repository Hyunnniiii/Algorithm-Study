# 자식 노드 2개 합쳐서 부모 노드 > 후위
def node(n):
    # 종료 조건
    if 0 < n <= N:
        # 왼쪽
        node(2*n)
        # 오른쪽
        node(2*n + 1)
        # 중앙
        # 리프 노드 2개일 때
        if 2*n <= N and 2*n + 1 <= N:
            tree[n] = tree[2*n] + tree[2*n + 1]

        # 리프 노드가 1개인 경우
        elif 2 * n <= N and 2 * n + 1 > N:
            tree[n] = tree[2*n]

for T in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)

    # 리프 노드 정보 입력받기
    for _ in range(M):
        lst = list(map(int, input().split()))
        tree[lst[0]] = lst[1]

    node(1)
    print(f'#{T} {tree[L]}')
