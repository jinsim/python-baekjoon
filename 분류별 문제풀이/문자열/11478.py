# 서로 다른 부분 문자열의 개수
"""
이중 for 문을 사용해서, 1, 12, 123, 1234, 12345, 2, 23, 234, ... 이런 식으로 모든 부분 문자열을 set에 추가하여 중복을 제거했다.
"""

word = input()
s = set()

len_word = len(word)
for i in range(len_word):
    for j in range(i, len_word):
        s.add(word[i:j+1])

print(len(s))
