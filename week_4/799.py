def min_time_to_serve(n, k, a):
    time = 0
    for i in range(k):
        time += a[i]
    return time

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(min_time_to_serve(n, k, a))
