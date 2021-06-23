weight = int(input())

arr_ref = [False] * 201

for i in range(2, 100, 2):
    for j in range(2, 100, 2):
        arr_ref[i + j] = True

if arr_ref[weight]:
    print("YES")
else:
    print("NO")