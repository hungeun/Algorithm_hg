n = int(input())

def h(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        h(n - 1, a, c, b)
        print(a, c)
        h(n - 1, b, a, c)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
h(n, 1, 2, 3)