

''' 술래잡기 체스 / 20260901 / 체감 난이도 : 골드 4 이상
소요 시간: 시간 / 시도: 1회 / 실행 시간: ms (코드트리) / 메모리: MB

[타임라인]
# 09:02 - 09:23(21분) 문제 읽기 / 입력 받기 / 구상
# 09:23 -

[구상]
    - 읽자마자 절망. 또 백트래킹임. 심지어 어제와 다르게 백트래킹을 하지 않는 풀이 따위 떠오르지 않음.
    하지만 이렇게 안하는게 생기는건 아주 위험하므로 못 풀더라도 백트래킹으로 풀기로 다짐함..
    - 문제가 길어서 읽다가 계속 위로 올리게 된다.. 그래서 앞으로는 그냥 주석에 쓰면서 문제를 봐야겠다
    - 배열이 4x4라서 충분히 완탐 가능해보였고, 내가 백트래킹만 온전히 구현해낸다면.. 못 풀 것 같진 않다는 생각이 들었음.

[구현]
- (good)
    - 백트래킹이 디버깅이 어렵다보니.. 그냥 모든 처리 중간중간에 print문 넣어서 다 확인했다.
    배열 복구를 안해서 문제가 생기고 있었음을 빠르게 알 수 있었다.

- (bad)
    - 구상할 떄는 괜찮았는데 막상 도둑들이 이동하는 함수를 구현하다보니 여러 문제가 생김
    1) 이미 술래가 잡은 도둑 번호에 대한 처리를 안해서 무한 루프 돌았고
    2) idx에 해당하는 도둑을 찾으면 바로 break 한 다음에 (0,0)부터 다시 시작해야 하는데
    break를 하면 for col- 부분만 정지돼서 그거에 대한 보수(?)를 하려다 보니 status를 쓰게 되면서..
    점점 함수가 복잡해짐

    - 백트래킹 복구할 때.. 술래가 원래 있던 곳, 이동한 곳만 다시 복구해주는 코드로 처음 구현했는데
    그렇게 하면 doduk 함수로 인해 또 배열이 바뀐 뒤에 복구를 해버리는 이상한 현상이 일어나기 때문에
    배열 복사로 해결함. 근데 진짜 백트래킹 너무 어려움

    리팩토링을 통해 배워갈 게 많을 예정

---------------------------------------------------------
[개선할 사항]
- 도둑 함수가 너무 복잡하다. 단순화해야함

'''
# =======================================================
# 술래말 하나로 도둑을 잡는다.
# 도둑말을 잡으면, 그 도둑말의 방향을 가지게 된다.

# [0] (0,0) 도둑말 잡고 시작
# [1] 도둑말: 번호가 작은 순서대로, 본인이 가진 이동 방향으로 이동. 한번에 한칸.
# 이때 45도 반시계 회전하면서 이동할 수 있을 때까지 탐색. 이동 못하면 그대로.
# 술래말이 있거나, 범위 벗어난 곳은 못 간다
# 이동한 곳에 말이 있으면, 그 말이랑 위치를 바꾼다

# [2] 술래말: 이동 가능한 방향의 어느 칸이나 선택해서 이동 가능. 한번에 여러칸 이동 가능
# 단 도둑말이 없는 곳으로는 이동 불가
# 잡으려고 가는 도중에 만나는 말은 잡지 않는다.
# 잡는 도둑말의 번호만큼 점수 획득

# [3] 종료: 술래말이 이동할 수 있는 곳에 도둑말이 더이상 없을 때

# 구할 것: 얻을 수 있는 점수의 최댓값


# import pprint

## 입력 받기
arr = [[(0,0)]*4 for _ in range(4)]
for idx in range(4):
    lst = list(map(int, input().split()))
    for iidx in range(4):
        arr[idx][iidx] = (lst[2*iidx], lst[2*iidx+1]-1)

di = [-1,-1,0,1,1,1,0,-1]
dj = [0,-1,-1,-1,0,1,1,1]


## 실행
# 함수: 도둑말 이동
def doduk():
    status = False
    idx = 1     # 이동할 도둑의 번호
    while idx <= 16:
        for r in range(4):
            if idx in eat:
                idx += 1
                break

            if status:
                status = False
                break

            for c in range(4):
                if arr[r][c][0] == idx:
                    idx += 1
                    nr, nc = r + di[arr[r][c][1]], c + dj[arr[r][c][1]]

                    # 갈 수 있는 곳이면
                    if (0 <= nr < 4 and 0 <= nc < 4) and arr[nr][nc][0] != -1:
                        arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                        status = True
                        break

                    # 못 가는 곳이면 > 반시계 탐색, 되면 그 방향으로 바꿔주기
                    else:
                        for k in range(1, 8):
                            nr, nc = r + di[(arr[r][c][1]+k)%8], c + dj[(arr[r][c][1]+k)%8]
                            if (0 <= nr < 4 and 0 <= nc < 4) and arr[nr][nc][0] != -1:
                                arr[r][c] = (arr[r][c][0], (arr[r][c][1] + k)%8)
                                arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                                status = True
                                break
    return

# 초기 세팅
sulle_information = (-1, arr[0][0][1])    # 술래 번호, 방향 인덱스
sulle_coord = (0,0)     # 술래 좌표
eat = []    # 술래가 먹은 번호 리스트
eat.append(arr[0][0][0])
arr[0][0] = sulle_information

ans = 0
# 전체 함수: 백트래킹
def btrk(sr, sc, sulle_inf):    # 술래 좌표, 술래 표시 및 방향
    global ans, arr

    # [1] 도둑말들 이동
    doduk()
    cur_arr = [brr[:] for brr in arr]   # 도둑말 이동 후의 상태 저장

    # [2] 술래말 이동
    cant_go = 0
    for k in range(1,4):
        arr = [crr[:] for crr in cur_arr]   # 선택한 k마다 배열 복구
        nr, nc = sr + di[sulle_inf[1]]*k, sc + dj[sulle_inf[1]]*k

        # 범위 내에 있고, 도둑말이 있다면 갈 수 있다
        if (0 <= nr < 4 and 0 <= nc < 4) and arr[nr][nc][0] > 0:
            # 처리
            sulle_num, sulle_dir = arr[nr][nc]      # 술래 새로운 위치로 이동
            eat.append(sulle_num)          # 먹은 말 기록

            arr[sr][sc] = (0, arr[sr][sc][1])       # 술래가 있던 곳 빈칸 처리
            arr[nr][nc] = (-1, arr[nr][nc][1])      # 술래가 이동한 곳 처리

            btrk(nr, nc, arr[nr][nc])

            a = eat.pop()   # 되돌아왔을 때 술래가 먹었던 것 취소

        else:
            cant_go += 1

    # [3] 술래가 갈 수 있는 곳이 없으면 종료
    if cant_go == 3:
        ans = max(ans, sum(eat))
        return

btrk(sulle_coord[0], sulle_coord[1], sulle_information)
print(ans)