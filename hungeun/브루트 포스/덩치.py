a = int(input())
b = []

for _ in range(a):
    weight, height = map(int, input().split())
    b.append((weight, height))

for i in b:
    rank = 1
    for j in b:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")