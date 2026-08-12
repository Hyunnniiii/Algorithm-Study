# N 은 10,000 이하의 자연수 -> O(N^2)은 위험할 수 있다
# float는 비교 및 연산에 시간이 오래 걸린다
# 한 개 이상 연속된 수들의 곱

N = int(input())
lst = list(float(input()) for _ in range(N))

max_mult = 0
# 왼쪽부터 한 개씩 늘려가면서 곱한 뒤 비교
for i in range(N):
    max_num = lst[i]

    # N번째 경우 처리
    if i == N - 1:
        b = 0
    else:
        b = lst[i] * lst[i + 1]

    # 1개씩 늘려가면서 곱한다
    for j in range(i, N - 2):
        if max_num < b:
            max_num = b
        b = b * lst[j + 2]

    if max_mult < max_num:
        max_mult = max_num

print(f"{max_mult:.3f}")

# ========
# 시작점 i마다 뒤쪽 숫자를 전부 곱해서 확인하는 방식은 시간초과가 날 가능성이 높다.
# 다른 방법: 현재 숫자에서 새로 시작할지, 앞의 연속곱에 현재 숫자를 이어 붙일지만 비교
N = int(input())
first = float(input())
cur = first     # 현재 숫자에서 끝나는 연속곱 중 최댓값
answer = first  # 전체에서의 최댓값

for _ in range(N-1):
    x = float(input())

    #
    cur = max(x, cur * x)
    answer = max(answer, cur)

print(f'{answer:.3f}')

# ======
# 여태까지 곱한 값이 1보다 작으면 그냥 리셋하고 뒤에꺼부터 시작하는 게 낫다 -> dp
mul = 1.0
for i in range(N):
    if mul < 1.0:
        mul = lst[i]
    else:
        mul *= lst[i]
    ans = max(f'{ans:.3f}')