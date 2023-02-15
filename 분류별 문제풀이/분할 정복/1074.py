N, r, c = map(int, input().split())

two_n = 2**N
table = [[0,1],[2,3]]
def z(y, x, size, val):
    if size == 1:
        return (table[r-y][c-x] + val)
    tmp_val = 2**((size-1)*2)
    tmp_size = (2**size)//2
    if r < y+tmp_size:
        if c < x+tmp_size:
            return z(y, x, size-1, val)
        else:
            return z(y, x+tmp_size, size-1, val+tmp_val)
    else:
        if c < x+tmp_size:
            return z(y+tmp_size, x, size-1, val+tmp_val*2)
        else:
            return z(y+tmp_size, x+tmp_size, size-1, val+tmp_val*3)
print(z(0, 0, N, 0))


