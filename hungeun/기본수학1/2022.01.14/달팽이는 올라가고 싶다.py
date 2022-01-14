a,b,v = map(int,input().split())
c = (v - b) / (a - b)

print(int(c) if c == int(c) else int(c) + 1)
        