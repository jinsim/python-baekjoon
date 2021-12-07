# 관점을 바꾸면 더 쉽게 풀 수도 있음.
""" -1짜리 배열을 만들고 입력값을 역순으로 정렬해서 해당 문자열의 번호에 맞게 값을 업데이트"""
l = [-1]*26
a = input()
for i, v in enumerate(a[::-1]):
    l[ord(v)-97] = len(a)-i-1

for i in l:
    print(i, end=' ')
