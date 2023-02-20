# Counter를 굳이 쓰지 않아도 된다.
from collections import Counter
a = Counter(input().upper()).most_common()
print(a[0][0] if len(a) == 1 else('?' if a[0][1] == a[1][1] else a[0][0]))
