arr = []
for i in range(9):
    arr.append(int(input()))
 
max = max(arr)
print(max)
idx = arr.index(max)
print(idx+1)

#리스트에서 최고값을 출력하는 함수 max()
#리스트에서 최소값을 출력하는 함수 min()
#리스트에 해당 값의 offset을 반환하는 index()메서드 함수