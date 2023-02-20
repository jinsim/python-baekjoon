# DP에 대한 이해가 필요한 예제. 인터리빙 문자열을 판독하는 함수이다.
# 메모이제이션, 타뷸레이션 각각 나눠서 풀이하였다.

"""
메모이제이션
재귀 호출을 위한 함수 rec을 선언하는데, 파라미터로는 a, b, c에서 지금까지 선택된 인덱스를 나타내는 i, j, k를 넣는다. 
len_a, len_b, len_c와 효율적인 프로그래밍을 위해 선언한 mem 등 rec()에서도 사용하고 is_interleaving_string_rec()는 1문제 당 1번 호출되므로, 해당 함수 내에 rec을 선언해준다.

i, j, k가 len_a, len_b, len_c와 같아지면 모든 문자열의 끝까지 온 경우이므로 1을 반환한다.

했던 작업을 반복하지 않기 위해 rec(i, j, k)의 결과를 mem에 딕셔너리로 저장해둘 것이다. 따라서 튜플 (i, j, k)가 이미 mem에 있는 경우에는 바로 값을 반환한다.

ans를 0으로 할당하고, i가 len_a보다 작으면서 a와 c의 현재 값이 같다면, ans에 결과값을 더해준다.
j가 len_b보다 작으면서 b와 c의 현재 값이 같다면, ans에 결과값을 더해준다.

맨 처음 rec(0,0,0)을 실행하게 된다면 a와 b에서 둘 중 하나를 선택하거나 둘 다를 선택하며 rec이 각각의 인덱스를 담고 퍼져나갈 것이다. 
False인 경우에는 i, j, k가 len_a, len_b, len_c와 같다는 조건이 끝까지 충족되지 않을 것이므로 0이 반환될 것이다.
True인 경우에는 조건이 충족되어 ans에 1이 더해져서, 0보다 큰 정수가 되면 결과적으로 bool을 거쳐 True가 반환될 것이다.
"""
for i in range(1, int(input())+1):    
    a, b, c = input().split()
    len_a, len_b, len_c = len(a), len(b), len(c)
    memo = {}

    def rec(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        if i == len_a and j == len_b and k == len_c:
            return True
        ans = 0 
        if i<len_a and a[i] == c[k]:
            ans += rec(i+1, j, k+1)
        if j<len_b and b[j] == c[k]:
            ans += rec(i, j+1, k+1)
        memo[(i, j, k)] = ans

        return(ans)
    print(f'Data set {i}: yes' if rec(0,0,0) else f'Data set {i}: no')

"""타뷸레이션 
a, b, c의 길이를 len_a, len_b, len_c로 저장해둔다.
만약 a와 b의 길이를 더한 값이 c의 길이와 같지 않다면 False를 바로 반환해준다.

dp를 위해서 가로의 길이는 len_b+1만큼, 세로의 길이는 len_a+1만큼의 2차원 배열을 만든다.
이때, 각 인덱스는 해당 문자열에서 아무것도 선택 안하면 0, 문자열 끝까지 갔으면 문자열의 길이를 나타내므로 +1을 해주어야 한다.

각 경우에서 직전 값을 참고하므로, 첫번째 행과 첫번째 열 각각의 상황에서 직접 반복문을 돌려주어야 한다. 이때 True가 나오는 경우는 특정 문자열과 결과의 앞부분이 동일한 경우이다.

그 다음엔 이중 반복문을 돌리면서, 이전 열(좌로 1칸)의 값이 True면서 열의 기준이 되는 b의 현재 값이 c의 현재 값과 같을 때. 혹은 이전 행(위로 1칸)의 값이 True면서 행의 기준이 되는 a의 현재 값이 c의 현재 값과 같을 때 True를 반환한다.
여기서 현재 값이란, a는 i-1, b는 j-1. c는 i+j-1을 나타낸다.  
좀 더 자세하게는, 2차원 배열에서 a, b 는 각각 열과 행을 나타내며, i, j는 a,b의 현재까지 선택한 문자열 개수를 나타낸다.
자세한 2차원 테이블 구조는 아래를 참고하면 좋다.

      ''    'b'   'bb'  'bbc' 'bbca'     
''
'b'
'bc'
'bcc'

"""
for z in range(1, int(input())+1):    
    a, b, c = input().split()
    len_a, len_b, len_c = len(a), len(b), len(c)
    dp = [[False]*(len_b+1) for _ in range(len_a+1)]
    dp[0][0] = True
    for i in range(1, len_a+1):
        if dp[i-1][0] and a[i-1] == c[i-1]:
            dp[i][0] = True 
    for j in range(1, len_b+1):
        if dp[0][j-1] and b[j-1] == c[j-1]:    
            dp[0][j] = True
    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if (dp[i-1][j] and c[i+j-1]==a[i-1]) or (dp[i][j-1] and c[i+j-1]==b[j-1]):
                dp[i][j] = True
    print(f'Data set {z}: yes' if dp[-1][-1] else f'Data set {z}: no')