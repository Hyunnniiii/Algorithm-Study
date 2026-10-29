''' 택배 하차 / 20260929 / 체감 난이도 : 골드 3
소요 시간: INF / 시도: 1회 / 실행 시간: 197ms (코드트리) / 메모리: 23MB

오늘 이 문제 너무 아프다

일단 난 문제를 보자마자 속으로 너무 좋아했는데,
전날 밤에 중력 템플릿 작성하면서 블록 중력까지 공부했었기 때문이다.
그리고 문제를 보자마자 아이디어가 떠올랐다
: 왼쪽/오른쪽 그냥 회전해서 중력 쓰면 되는거 아님? 크크
이럼서 시작했다

사실 여기까지는 문제가 없었는데
묘수 써서 망했다.
직사각형 좌표 들고 다니면 무거울 것 같아서 행 정보만 저장했다. 이유는..
회전하면 행 번호가 열 번호로 바뀌기 때문에.
근데 결국 직사각형 아래로 내리려면 행,열 정보 다 필요하고.. 이걸 구상 단계에서
충분히 생각하지 않았기 때문에 구현하던 중간에 열 정보까지 추가하면서 내가 진짜 싫어하는
내 코드를 내가 구현하는데 이 변수가 뭐였더라? 하는 참사가 일어났다.

구현하면서 복잡하면 다시 생각하라고 그게 아닌거라고
밀고 나가지 말라고 버티지 말라고

좀만 일찍 포기했으면 좋았을텐데 테케 1, 2번만 딱 맞는 코드를 12시 쯤에 겨우 완성했던 것 같다
3번 테케에서 바로 틀렸고.. 3번 테케는 30x30 대왕 테케였다

보자마자 디버깅 절대 불가임을 깨달았고
그냥 코드 다 엎었다
수정할 자신도 없고. 내 코드 설명하래도 못하겠는데 이걸 어떻게 수정하겠음

그 뒤로는 정말 무식하게 구현했는데 시간에 너무 쫓겨서 사실 무슨 정신으로 코드를 친건지
기억이 잘 나지 않는다..
시험 때였으면 더 당황했을 것이기 때문에 정말 이래선 안된다

진짜 괜히 머리쓰지 말고 그냥 하자
그리고 아닌 것 같으면 빠르게 빠꾸. 제발


[결론]
진심 구상할 때는 무조건 풀 줄 알았다.
오늘부로 선포한다 루틴 제 0 원칙
흥 분 절 대 금 지
묘 수 절 대 금 지
정 직 하 게 살 자
성 실 하 게 살 자
자 만 하 지 말 자
깝 죽 대 지 말 자

특히. 난 인덱싱에 너무 약함. 좌표 변환하는거 진짜 지양해라. 그냥 돌려서 새로 계산해

'''

# 직사각형을 아래로 처 내린다
def put_box_down(idx, arr, coords):
    bottom = max(r for r,c in coords)
    cols = sorted(set(c for r, c in coords))

    # 얼마나 내려갈 수 있는지 확인
    move = 0
    for row in range(bottom+1, len(arr)):
        if all(arr[row][c]==0 for c in cols):
            move += 1
        else:
            break

    if move==0:
        return coords

    # 기존 위치 삭제
    for r, c in coords:
        arr[r][c] = 0

    # 새로운 좌표 저장, 배열에 표시
    new_coords = []
    for r, c in coords:
        arr[r+move][c] = idx
        new_coords.append((r+move, c))
    return new_coords


# 배열에서 직사각형 좌표 구하기
def get_coords(arr):
    info = {}

    for r in range(N):
        for c in range(N):
            idx = arr[r][c]

            if idx==0:
                continue

            if idx not in info:
                info[idx] = []
            info[idx].append((r,c))
    return info


# 이미 직사각형 들어있을 때 중력 적용하기
def gravity(arr):
    box_info = get_coords(arr)

    # 아래쪽 박스부터 내려야 하니까 정렬
    order = sorted(box_info.keys(),
                   key = lambda x : max(r for r,c in box_info[x]),
                   reverse = True)

    # 아래쪽부터 중력 적용, 새로운 좌표 얻기
    for idx in order:
        box_info[idx] = put_box_down(idx, arr, box_info[idx])


def debug_print(word):
    print(word)
    for row in arr:
        print(row)
    print()


################################
N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
boxes = []
for _ in range(1, M+1):
    idx, sero, garo, col = map(int, input().split())
    boxes.append((idx,sero,garo,col-1))


# [1] 박스 채워넣기
for idx, sero, garo, col in boxes:
    coords = []

    # 박스 일단 위에 두기
    for r in range(sero):
        for c in range(col, col+garo):
            arr[r][c] = idx
            coords.append((r,c))

    # 이제 아래로 내려
    put_box_down(idx,arr,coords)


# [2] 다 사라질 때까지 좌/우
while True:
    # (1) 왼쪽
    imsi = [list(row[:]) for row in zip(*arr)][::-1]    # 반시계

    # 중력 적용
    gravity(imsi)

    # 이제 맨 밑에 있는 박스들 확인
    remove_lst = set()
    for c in range(N):
        if imsi[N-1][c] != 0:
            remove_lst.add(imsi[N-1][c])

    # 제거할게 있으면 없애요
    if remove_lst:
        print(min(remove_lst))
        for r in range(N):
            for c in range(N):
                if arr[r][c] == min(remove_lst):
                    arr[r][c] = 0

    # 중간점검
    if sum(map(sum, arr)) == 0:
        break

    # 중력
    gravity(arr)

    # ========
    # (2) 오른쪽
    imsi = [list(row[:]) for row in zip(*arr[::-1])]

    # 중력 적용
    gravity(imsi)

    # 이제 맨 밑에 있는 박스들 확인
    remove_lst = set()
    for c in range(N):
        if imsi[N - 1][c] != 0:
            remove_lst.add(imsi[N - 1][c])

    # 제거할게 있으면 없애요
    if remove_lst:
        print(min(remove_lst))
        for r in range(N):
            for c in range(N):
                if arr[r][c] == min(remove_lst):
                    arr[r][c] = 0

    # 중간점검
    if sum(map(sum, arr))==0:
        break

    # 중력
    gravity(arr)

