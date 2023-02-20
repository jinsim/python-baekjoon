from collections import Counter
dic = {"A": 0, "C":0, "G":0, "T":0}

S, P = map(int, input().split())
DNA = input()
dic["A"], dic["C"], dic["G"], dic["T"] = map(int, input().split())

start = 0
ret = 0
cnter = Counter(DNA[:P])

for word in dic:
    cnter[word] -= dic[word]
if not -cnter:
    ret += 1

while start < S-P:
    cnter[DNA[start]] -= 1
    cnter[DNA[P + start]] += 1
    if not -cnter:
        ret += 1
    start += 1
print(ret)

