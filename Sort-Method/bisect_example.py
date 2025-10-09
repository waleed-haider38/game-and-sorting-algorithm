import bisect
arr = [10, 20, 30, 40]
pos = bisect.bisect_left(arr, 25, 0, len(arr))
print(pos)
