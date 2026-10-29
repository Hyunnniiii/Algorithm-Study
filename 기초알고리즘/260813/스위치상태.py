N = int(input().strip())    # 스위치의 개수
switch = list(map(int, input().split()))    # 스위치 초기 상태
S = int(input().strip())    # 학생 수

# 스위치 바꾸는 함수 정의
def change(i):
    if switch[i] == 1:
        switch[i] = 0
    elif switch[i] == 0:
        switch[i] = 1

for _ in range(S):
    # 성별, 받은 스위치 번호
    sex, idx = map(int, input().split())    # 남자1 여자2

    # 남자일 때
    if sex == 1:
        # 배수인 스위치를 바꾼다 (인덱스 주의)
        for x in range(idx-1, N):
            if (x+1) % idx == 0:
                change(x)

    # 여자일 때
    if sex == 2:
        # 먼저 본인 스위치 바꾸고
        change(idx-1)

        # 양쪽 대칭 확인
        status = True
        while status:
            for k in range(1, min(N-idx, idx-1)+1):
                if switch[idx-1-k] == switch[idx-1+k]:
                    change(idx-1-k)
                    change(idx-1+k)

                elif switch[idx-1-k] != switch[idx-1+k]:
                    status = False
                    break
            break

# 20개씩 출력하기
a = len(switch) // 20

for i in range(a):
    print(*switch[20*i : 20*(i+1)])
print(*switch[20*a:])