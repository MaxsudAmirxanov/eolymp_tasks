def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = []
    equal = []
    greater = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quicksort(less) + equal + quicksort(greater)

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
sorted_arr = quicksort(arr)
for num in sorted_arr:
    print(num)
