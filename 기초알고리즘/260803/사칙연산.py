# 중위 순회. 리프 노드에만 숫자가 있다
# 완전 이진 트리가 아니다 -> 좌/우/연산 칸에 대한 배열 생성
# 정수부분만 출력, 1<=N<=1000

def yunsan(n):
    # 종료하는 경우
    if n <= 0 or n > N:
        return tree[1]

    # 숫자인 경우
    if tree[n] not in ('+', '-', '*', '/'):
        return float(tree[n])

    # 연산자가 나오는 경우
    left_num = yunsan(left[n])
    right_num = yunsan(right[n])

    if tree[n] == '+':
        return left_num + right_num
    elif tree[n] == '-':
        return left_num - right_num
    elif tree[n] == '*':
        return left_num * right_num
    elif tree[n] == '/':
        return left_num / right_num


for T in range(1, 11):
    N = int(input())

    left = [0] * (N+1)  # 왼쪽 자식 노드
    right = [0] * (N+1)  # 오른쪽 자식 노드
    tree = [0] * (N+1)   # 연산자 및 계산 결과 표시용

    for _ in range(N):
        lst = list(input().split())

        if lst[1] in ('+', '-', '*', '/'):
            left[int(lst[0])] = int(lst[2])
            right[int(lst[0])] = int(lst[3])
            tree[int(lst[0])] = lst[1]
        else:
            tree[int(lst[0])] = int(lst[1])

    print(f'#{T} {int(yunsan(1))}')