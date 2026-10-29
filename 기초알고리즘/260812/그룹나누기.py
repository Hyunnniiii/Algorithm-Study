for TC in range(1, int(input())+1):
    # 출석번호(노드) N개 / 신청서(간선) M장
    N, M = map(int, input().split())

    # 대표 노드 표시할 리스트 (초기에는 자기 자신이 대표)
    student = [i for i in range(N+1)]
    # print(student)

    # 모두 union 한 다음에 묶음의 개수 구하기
    # union하기 위해 union / find 함수 정의
    def find(x):
        if student[x] != x:
            student[x] = find(student[x])
        return student[x]

    def union(x, y):
        a = find(x)
        b = find(y)

        student[b] = a

    # 신청서 리스트
    lst = list(map(int, input().split()))

    # 신청한 학생끼리 유니온
    for i in range(0, len(lst), 2):
        union(lst[i], lst[i+1])

    # 모두 합친 뒤 가장 대표 노드로 바꿔주기
    for i in range(1, N+1):
        student[i] = find(i)

    print(f'#{TC} {len(set(student[1:]))}')   # 0번 제외
