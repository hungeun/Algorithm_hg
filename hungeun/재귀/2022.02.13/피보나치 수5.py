n = [0,1]
n1 = 0
n2 = 0
num = int(input())
sum = 0
for i in range(2,num+1):
    n1=n[i-1]
    n2=n[i-2]
    k=n1+n2
    n.append(k)

print(n[num])