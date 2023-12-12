import time
a = int(input())
print(a)
def some_function(a):
    x = 1
    c = []
    while x <= a:
        c.append(x)
        x += 1
    return c
startt = time.time()
print(some_function(a))
endt = time.time()
print(startt-endt)