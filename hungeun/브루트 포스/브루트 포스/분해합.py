n = int(input())

for i in range(1,n+1):
    a = sum((map(int,str(i))))
    a_sum = i + a

    if a_sum == n:
        print(i)
        break
    if i == n:
        print(0)