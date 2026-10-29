for T in range(1, int(input())+1):
    # 문자열 분리해서 입력받기
    words = list(input())

    # 리스트 생성하고 알파벳을 하나씩 추가
    # 가장 마지막에 넣은 것-> ?? 이라기 보다는 top of stack과 같으면 둘 다 제거
    stk = []
    for x in words:
        if stk and stk[-1] == x:
            stk.pop()
        else:
            stk.append(x)
    print(f'#{T}', len(stk))


