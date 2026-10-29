N, K = map(int, input().split())    # N: 문자 수 / K: 실행 횟수

# 종협짱의 포인터: 알파벳 리스트 말고 인덱스를 가리키는 포인터만 옮기자
# 마지막에 가리키는 문자부터 출력

lst = ['?']*N
idx = 0
ans = '?'
for _ in range(K):
    move, alpha = map(str, input().split())
    move = int(move)    # 숫자로 바꿔주기

    # move에 나온 만큼 인덱스를 뒤로 옮긴다
    idx = idx - move

    # 인덱스 음수 되면 바꿔주기
    while idx < 0:
        idx += N

    # 입력된게 없었다면 알파벳 넣어준다
    # 문제 조건))))))))) 어떠한 문자도 두 번 이상 나오지 않는다!!!!!!!!!!
    if lst[idx] == '?':
        if alpha in lst:
            ans = '!'
            break
        else:
            lst[idx] = alpha


    # 입력된게 있는데 다르면 > 불가능
    if lst[idx] != '?':
        if lst[idx] != alpha:
            ans = '!'
            break

    # 입력된게 있는데 같으면 > 패스
        if lst[idx] == alpha:
            pass

if ans == '!':
    print(ans)
else:
    if idx == 0:
        for k in range(N):
            print(lst[k], end='')

    else:
        for k in range(idx, N):
            print(lst[k], end='')
        for j in range(0, idx):
            print(lst[j], end='')
