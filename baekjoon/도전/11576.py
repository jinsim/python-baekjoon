A, B = map(int, input().split())
m = int(input())
num_A = list(map(int, input().split()))
num_10 = 0

# for i in range(m):
#     num_10 += (A**i) * num_A[i]
for i in num_A:
    num_10 += i * A**(m-1)
    m-=1

num_B = []
# while num_10 >= B:
#     num_B.append(num_10%B)
#     num_10 = num_10//B
# num_B.append(num_10)
# num_B.reverse()
# print(*num_B)
while num_10:
    num_B.append(num_10%B)
    num_10 //= B
print(*num_B[::-1])