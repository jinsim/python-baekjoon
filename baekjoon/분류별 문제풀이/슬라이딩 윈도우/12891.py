cnter = {"A": 0, "C":0, "G":0, "T":0}
dic = {"A": 0, "C":0, "G":0, "T":0}
S, P = map(int, input().split())
DNA = input()
for word in DNA[:P]:
    cnter[word] += 1
dic["A"], dic["C"], dic["G"], dic["T"] = map(int, input().split())

start = 0
ret = 0

for word in dic:
    cnter[word] -= dic[word]
if min(cnter.values()) >= 0:
    ret += 1

while start < S-P:
    cnter[DNA[start]] -= 1
    cnter[DNA[P + start]] += 1
    if min(cnter.values()) >= 0:
        ret += 1
    start += 1
print(ret)

