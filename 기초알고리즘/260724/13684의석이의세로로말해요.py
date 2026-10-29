for test_case in range(1, int(input())+1):
    arr = [[]*15 for _ in range(5)]
    for i in range(5):
        arr[i] = list(map(str, input()))

# 위의 3줄 아래로 대체 가능
# arr = [list(input()) for _ in range(5)]

    # arr에서 가장 길이가 긴 문자열 길이 찾기
    max_lgth = 0
    for x in arr:
        if len(x) >= max_lgth:
            max_lgth = len(x)
    # 빈 자리에 공백 채우기
    for x in arr:
        if len(x) < max_lgth:
            x.extend([' '] * (max_lgth - len(x)))

    # 세로로 읽기
    print(f'#{test_case}', end=' ')
    for j in range(max_lgth):
        for i in range(5):
            if arr[i][j] != ' ':
                print(arr[i][j], end='')
    print()

# ans = ''
# for j in range(15):
#     for i in range(5):
#         if j >= len(arr[i]):
#             continue
#             ans += arr[i][j]
# print(f'#{t} {ans}')