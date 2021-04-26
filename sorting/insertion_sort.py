
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > value:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = value
    return arr


t1 = [7, 1, 3, 5]
t2 = [4, 2, 5, 1, 3]
t3 = [5, 4, 4, 7, 9, 0, 46]
tests = [t1, t2, t3]
for t in tests:
    print(t)
    print(insertion_sort(t))
