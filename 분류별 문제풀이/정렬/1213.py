# 딕셔너리를 사용한 풀이법
"""
1. input()안의 각 글자를 defaultdict에 넣어 개수를 센다.
2. 딕셔너리 각 요소를 가져와서 개수를 파악하는데, 홀수가 2개면 안된다.
3. 홀수인 글자는 center_word에 넣어두고, 나머지 글자들은 words에 문자 개수를 2로 나눈 몫만큼 넣어둔다. 
4. 사전순 출력이므로, words를 정렬해서 다시 문자열로 만든다.
5. 팰린드롬 제작
"""
from collections import defaultdict

dic = defaultdict(int)
for i in input():
   dic[i] += 1

cnt = 2
center_word = ''
words = ''

for i in dic:
    if dic[i] % 2 == 1:
        cnt -= 1
        if not cnt:
            print("I'm Sorry Hansoo")
            break
        center_word = i
    words += i*(dic[i]//2)

words = ''.join(sorted(words))

if cnt:
    print(words + center_word + words[::-1])