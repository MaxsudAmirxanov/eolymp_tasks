def count_swaps(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    swaps = count_swaps(arr)
    print(f"Optimal train swapping takes {swaps} swaps.")
