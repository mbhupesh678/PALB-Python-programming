arr = [1, 4, 3, 5, 8, 6]
min_val = arr[0]
max_val = arr[0]

for i in range(len(arr)):
    if arr[i] < min_val:
        min_val = arr[i]
    else:
        if arr[i] > max_val:
            max_val = arr[i]

print("Minimum:", min_val)
print("Maximum:", max_val)
