def x(a): 
    if a <= 0: 
        return 1 
    return a*x(a-1)
    

b= int(input())

result = x(b)

print(result) 