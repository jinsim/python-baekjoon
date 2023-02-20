from functools import reduce
print(reduce(lambda x, y: x+y, range(int(input())+1)))
