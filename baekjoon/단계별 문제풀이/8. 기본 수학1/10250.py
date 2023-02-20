# 계산 후에 코드 작성하기. 기준이 뭔지 파악하고, 예외 상황을 발견할 것 
"""
층 수는 나머지, 호 수는 몫이다. 이때 10이하면 앞에 0이 있어야하므로 zfill을 사용한다.
나머지가 0인 경우를 예외처리 해주어야한다.
"""
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    a = n % h
    if a:
        print(a, str(n//h+1).zfill(2), sep='')
    else:
        print(h, str(n//h).zfill(2), sep='')
