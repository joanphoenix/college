def potn(x, n):
    if n == 0:
        return 1
    else:
        return x * potn(x, n - 1)


print(potn(2, 10))
