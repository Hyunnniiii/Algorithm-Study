N, M, S = map(int, input().split())

def jowa(cnt, sm, lst):
    # 종료조건: M개 선택
    if cnt == M and sm == S:
        print(*lst)
        return
    elif cnt == M and sm != S:
        return

    # 중복 허용해서 숫자 선택하기
    for k in range(1, N+1):
        jowa(cnt+1, sm+k, lst+[k])
jowa(0,0,[])
