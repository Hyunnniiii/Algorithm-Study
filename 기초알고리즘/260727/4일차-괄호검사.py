for T in range(1, int(input())+1):
    txt = list(input())

    # 괄호만 남기기
    lst = []
    for i in txt:
        if i in ['(', ')', '{', '}']:
            lst.append(i)

    nlst = []
    answer = 1
    for x in lst:
        # (, { 가 나오면 리스트에 추가
        if x == '(' or x == '{':
            nlst.append(x)

        # ), } 가 나왔을 때
        else:
            # 빈 스택에 닫는 괄호로 시작하면 break
            if not nlst:
                answer = 0
                break

            # top과 비교해서 괄호 성립하면 pop
            if x == ')' and nlst[-1] == '(':
                nlst.pop()
            elif x == '}' and nlst[-1] == '{':
                nlst.pop()
            else:
                answer = 0
                break

    # 완료한 뒤 열린 괄호 남아있으면 실패
    if nlst:
        answer = 0
    print(f'#{T} {answer}')