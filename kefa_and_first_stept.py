n = int(input())
m = list(map(int, input().split()))

length = 1  
max_length = 1  

for i in range(1, n):
    if m[i] >= m[i-1]:
        length += 1
    else:
        length = 1
    max_length = max(max_length, length)

print(max_length)