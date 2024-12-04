def mdc(m, n):
    if m % n == 0:
        return n
    else:
        return mdc(n, m % n)
    
print(mdc(48, 30))