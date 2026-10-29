# 제약사항: 3 <= N <= 10 -> 10*N으로 하면 무조건 갱신된다
# visit으로 처리한다면? : 덜 무식한 방법
def dfs(cnt, sm):
    global min_sm
    # 종료 조건: N개 고르면 끝
    if cnt == N:
        if sm < min_sm:
            min_sm = sm
        return

    # 숫자 고르기: 한줄에 하나만-> visit으로 해보면??
    for j in range(N):
        if visit[j] == 0:
            visit[j] = 1
            dfs(cnt+1, sm + arr[cnt][j])
            visit[j] = 0

for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    min_sm = 10 * N

    dfs(0,0)
    print(f'#{T} {min_sm}')


# ======
# 첫 풀이

def dfs(cnt, sm, ilst, jlst):
    # 종료 조건: N개 고르면 끝
    if cnt == N:
        lst.append(sm)
        return sm
    # 숫자 고르기: 한줄에 하나만
    for i in range(N):
        for j in range(N):
            # 이렇게 i, j를 다 리스트에 추가해서 하면 비효율. 이러면 안됨
            # v 안에 i, j가 있는지 일일히 찾는게 오래 걸린다
            if i not in ilst and j not in jlst:
                dfs(cnt + 1, sm + arr[i][j], ilst + [i], jlst + [j])

for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []

    dfs(0, 0, [], [])
    print(f'#{T} {min(lst)}')




