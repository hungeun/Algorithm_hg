# def prime_list(n):
#     sieve = [True] * n
    
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:
#             for j in range(i + i, n , i):
#                 sieve[j] = False
    
#     return [ i for i in range(2,n) if sieve[i] == True] 
# ==================에라토스테네스의 체 ======================

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)