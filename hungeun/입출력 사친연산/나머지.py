input_data = input().split(' ')
a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])

print(int((a + b)%c))
print(int(((a % c)+(b % c)) %c))
print(int((a * b) % c))
print(int(((a % c) * (b % c)) %c))
