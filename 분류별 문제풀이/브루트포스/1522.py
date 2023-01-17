string = input()
len_str = len(string)
num = string.count('a')
min_num = num
string *= 2
for i in range(len_str):
    min_num = min(string[i:i+num].count('b'), min_num)
print(min_num)