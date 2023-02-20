import sys

#표준입력을 파일로 설정
sys.stdin = open("../../input.txt","r")
N = int(input())
max_cnt = -1
ret = []

def get_pre_cnt(x, y):
    cnt = 0
    for i in range(0, min(len(x), len(y))):
        if x[i] == y[i]:
            cnt += 1
        else:
            break
    return cnt

word_list = sorted([(input(), i) for i in range(N)])
# print(word_list)
for i in range(N-1):
    x = word_list[i]
    y = word_list[i+1]
    if x == y:
        continue
    # print(x, y, ret)
    pre_cnt = get_pre_cnt(x[0], y[0])
    # print(pre_cnt, max_cnt)

    if pre_cnt == max_cnt:
        # print(2)
        # 새로 들어온 x y의 인덱스가 더 빠른 경우
        if min(x[1], y[1]) < min([i[1] for i in ret]):
            # print(4)
            ret = [x, y]

        # 같은 접두사를 가진 단어가 이어서 3개 이상 나온 경우
        if x == ret[-1]:
            # print(3)
            ret.append(y)
            # ret.sort(key=lambda x:x[1])

    if pre_cnt > max_cnt:
        # print(1)
        max_cnt = pre_cnt
        # 인덱스순으로 정렬
        # ret = sorted([x, y], key=lambda x:x[1])
        ret = [x, y]

ret = sorted(ret, key=lambda x:x[1])
print(ret[0][0], ret[1][0], sep="\n")
# print(ret)

