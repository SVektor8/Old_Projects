def f(n):
    if (n>0):
        f(n-4)
        f(n//2)
        print(n, end='')
f(7)
