
def in_order(n):
    global num

    # 범위 내에 있을 때
    if 0 < n <= N:
        # 왼쪽
        in_order(2*n)
        # n: 노드 번호, num: 탐색 순서
        tree[n] = num
        num += 1
        # 오른쪽
        in_order(2*n + 1)

for T in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1

    in_order(1)
    print(f'#{T} {tree[1]} {tree[N//2]}')

