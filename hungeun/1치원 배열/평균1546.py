n = int(input())
score = list(map(float, input().split()))

max = 0 
for i in range(n):
    if max < score[i]:
        max = score[i]

for i in range(n):
    score[i] = (score[i] / max) * 100

sum = 0
for i in range(n):
    sum += score[i]

print(sum / n)

#https://wook-2124.tistory.com/237