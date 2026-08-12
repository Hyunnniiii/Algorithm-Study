N = int(input())
tree = [' '] + list(input())

def pre_order(n):
    if n <= 0 or n > N:
        return    # 종료조건

    print(tree[n], end='')  # 중심
    pre_order(2*n)  # 왼쪽
    pre_order(2*n + 1)  # 오른쪽

pre_order(1)