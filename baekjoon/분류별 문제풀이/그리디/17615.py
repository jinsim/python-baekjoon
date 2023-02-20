""" 실버 1 - 볼 모으기
각 단어가 제일 끝에 있을 때, 제일 끝에 있는 단어가 연결된 개수만큼을 단어의 전체 수에서 뺀다면, 그게 최소 이동의 개수이다.
끝에 있지 않은 단어가 끝에 가기 위해서는 단어의 전체 개수만큼 이동해야 한다.
결과에 대한 최적화는 아직 진행하지 못했다. 방법이 있을 듯
"""
N = int(input())
string = input()
R_cnt = string.count('R')
B_cnt = N-R_cnt

start_word = string[0]
start_cnt = 0
for i in range(N):
    if string[i] == start_word:
        start_cnt += 1
    else:
        break
end_word = string[-1]
end_cnt = 0
for i in range(N-1, -1, -1):
    if string[i] == end_word:
        end_cnt += 1
    else:
        break
if start_word == 'R':
    if end_word == 'R':
        print(min(R_cnt - start_cnt, R_cnt - end_cnt, B_cnt))
    else:
        print(min(R_cnt - start_cnt, B_cnt - end_cnt))
else:
    if end_word == 'R':
        print(min(B_cnt - start_cnt, R_cnt - end_cnt))
    else:
        print(min(B_cnt - start_cnt, B_cnt - end_cnt, R_cnt))
