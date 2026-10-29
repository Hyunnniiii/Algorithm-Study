N, P = map(int, input().split())

def cycle(x):
    # 종료 조건: 중복될 때 -> 중복된 숫자가 처음 나타난 위치를 빼준다
    # 반복되지 않는 부분이 1개 이상일 수 있다!!
    if x in lst:
        return len(lst)-lst.index(x)

    # 단위 행동
    lst.append(x)
    next_x = x * N % P
    return cycle(next_x)

lst = []
print(cycle(N))