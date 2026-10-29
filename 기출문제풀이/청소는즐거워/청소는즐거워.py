
''' 청소는 즐거워 / 20260826 / 체감 난이도 : 실버 5
소요 시간: 1시간 30분 / 시도: 1회 / 실행 시간: 384ms (코드트리) / 메모리: 27MB

[타임라인]
# 13:37 - 13:55(18분) 문제 읽기 / 구상
# 13:55 - 14:48(53분) 전체적인 구현 완료
# == 면담하고 옴 ==
# 15:14 - 15:29(15분) 검증, 코드 다듬기 후 제출

[구상]
- (good)
    - 이상한 체스 풀면서 어떤 함수를 만들 때 구상 단계에서 기능을 명확히 정하는게 좋겠다는 꺠달음을 바탕으로
    오늘 만든 함수는 어떤 역할을 하는지, 무엇을 출력해야 하는지 정확하게 정하고 들어감. 확실히 구현할 때 시간도
    훨씬 덜 걸리고 오류도 적다.

[구현]
- (good)
    - 딕셔너리를 적절히 잘 활용한 것 같다. 구상한 대로 구현이 되어줘서 감사하다..
    - 하드코딩을 두려워하지 말자는 마인드로 일반화하지 않고 비율 퍼센트에 따라 다 코드에 작성했는데,
    오히려 일반화하려 했다면 꼬였을 것 같다. 하드코딩은 기세다

[후기]
    - 솔직히 오늘은 내 코드가 맘에 듬 ㅎㅎ
    - 사실 코드리뷰는 회전빙하를 해야함. 심각하다..

---------------------------------------------------------
[개선할 사항]
- cal에 비율까지 저장해서 한 번에 계산 가능하게 할 수 있음
- 달팽이 구현 다른 방법 보기
- 다른 사람들 코드 보면서 공부
'''
# =======================================================

## 입력받기
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

## 필요한 요소들
# 우상좌하
di = [0,-1,0,1]
dj = [1,0,-1,0]

# 계산할 배열들 딕셔너리: 작은 비율부터
cal = {
    1 : [(1,-1), (1,1), (0,-2), (0,2), (-2,0), (0,-1), (0,1), (-1,-1), (-1,1), (-1,0)],     # 상
    3 : [(-1,-1), (-1,1), (0,-2), (0,2), (2,0), (0,-1), (0,1), (1,-1), (1,1), (1,0)],     # 하
    2 : [(-1,1), (1,1), (-2,0), (2,0), (0,-2), (-1,0), (1,0), (-1,-1), (1,-1), (0,-1)],     # 좌
    0 : [(-1,-1), (1,-1), (-2,0), (2,0), (0,2), (-1,0), (1,0), (-1,1), (1,1), (0,1)]      # 우
}

visit = [[0]*N for _ in range(N)]       # 방문한 곳 표시
import pprint
# 함수: 현재 위치에 따라 이동하는 함수
# 현재 방향을 기준으로 다음 방향 인덱스로 진행했을 때 visit이 0이면 그 쪽으로 방향을 틀어준다
# 다음 방향이 visit = 1이라면 현재 방향을 그대로 유지한다
# 함수로 얻을 것: visit 처리, 방향을 바꿀지 말지 > 방향 인덱스 반환

# 다만 이 함수는 첫 시작 처리를 잘 해야 한다
def wheretogo(si, sj, d_idx):
    ni, nj = si + di[(d_idx + 1)%4], sj + dj[(d_idx + 1)%4]     # 다음 방향으로 바꿨을 때 확인

    # 꺾었을 때 범위 내에 없거나 청소하지 않은 곳이라면 그쪽으로 변경
    if not (0 <= ni < N and 0 <= nj < N) or visit[ni][nj] == 0:
        d_idx = (d_idx + 1)%4

    return d_idx

## 실행
ans = 0         # 바깥으로 나간 먼지의 총량
cur_r, cur_c = N//2, N//2       # 중앙은 항상 N//2
visit[cur_r][cur_c] = 1
cur_d = 1       # 왼쪽 방향으로 진행 시작하도록 설정
status = True
while status:   # (0,0)에 갈 때까지 진행

    # [1] 원래 진행하던 방향으로 진행할 수 있는지 확인, 다음 칸으로 이동
    cur_d = wheretogo(cur_r, cur_c, cur_d)
    nxt_r, nxt_c = cur_r + di[cur_d], cur_c + dj[cur_d]
    visit[nxt_r][nxt_c] = 1

    # [2] 현재 진행 중인 방향에 따라 배열 숫자 계산 후 적용
    dust = arr[nxt_r][nxt_c]
    arr[nxt_r][nxt_c] = 0
    for_a = 0   # a% 계산을 위해
    for k in range(10):
        if k == 0 or k == 1:    # 1%
            plus = dust // 100
            x, y = cal[cur_d][k]

            # 더하려는 곳이 배열 안에 있다면
            if (0 <= nxt_r + x < N and 0 <= nxt_c + y < N):
                arr[nxt_r + x][nxt_c + y] += plus
                for_a += plus
            # 배열 밖이라면 > 정답에 저장
            else:
                ans += plus
                for_a += plus

        if k == 2 or k == 3:  # 2%
            plus = (dust * 2) // 100
            x, y = cal[cur_d][k]

            # 더하려는 곳이 배열 안에 있다면
            if (0 <= nxt_r + x < N and 0 <= nxt_c + y < N):
                arr[nxt_r + x][nxt_c + y] += plus
                for_a += plus
            # 배열 밖이라면 > 정답에 저장
            else:
                ans += plus
                for_a += plus

        if k == 4:  # 5%
            plus = (dust * 5) // 100
            x, y = cal[cur_d][k]

            # 더하려는 곳이 배열 안에 있다면
            if (0 <= nxt_r + x < N and 0 <= nxt_c + y < N):
                arr[nxt_r + x][nxt_c + y] += plus
                for_a += plus
            # 배열 밖이라면 > 정답에 저장
            else:
                ans += plus
                for_a += plus

        if k == 5 or k == 6:  # 7%
            plus = (dust * 7) // 100
            x, y = cal[cur_d][k]

            # 더하려는 곳이 배열 안에 있다면
            if (0 <= nxt_r + x < N and 0 <= nxt_c + y < N):
                arr[nxt_r + x][nxt_c + y] += plus
                for_a += plus
            # 배열 밖이라면 > 정답에 저장
            else:
                ans += plus
                for_a += plus

        if k == 7 or k == 8:  # 10%
            plus = dust // 10
            x, y = cal[cur_d][k]

            # 더하려는 곳이 배열 안에 있다면
            if (0 <= nxt_r + x < N and 0 <= nxt_c + y < N):
                arr[nxt_r + x][nxt_c + y] += plus
                for_a += plus
            # 배열 밖이라면 > 정답에 저장
            else:
                ans += plus
                for_a += plus

        if k == 9:     # a%
            plus = dust - for_a
            x, y = cal[cur_d][k]

            # 더하려는 곳이 배열 안에 있다면
            if (0 <= nxt_r + x < N and 0 <= nxt_c + y < N):
                arr[nxt_r + x][nxt_c + y] += plus
                for_a += plus
            # 배열 밖이라면 > 정답에 저장
            else:
                ans += plus

    # [3] 좌표 갱신
    cur_r, cur_c = nxt_r, nxt_c
    if cur_r == 0 and cur_c == 0:
        status = False
        break
print(ans)