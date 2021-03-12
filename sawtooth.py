

def countSawSubarrays(arr):
    n = len(arr)
    ans = 0
    saw = [0]*n

    if n == 0 or n == 1:
        return 0

    if n == 2:
        if (arr[0] > arr[1]) or (arr[1] > arr[0]):
            return 1
        else:
            return 0

    saw[0] = 0
    if (arr[0] > arr[1]) or (arr[1] > arr[0]):
        saw[1] = 2

    for i in range(2, n):
        if (arr[i-2] < arr[i-1] and arr[i-1] > arr[i]) or (arr[i-2] > arr[i-1] and arr[i-1] < arr[i]):
            if i == 2:
                saw[i] = saw[i-2] + 3
            else:
                saw[i] = saw[i-2] + 2
        elif arr[i-1] > arr[i] or arr[i] > arr[i-1]:
            saw[i] = 2

    for i in range(0, n):
        if saw[i] <= 0:
            continue
        ans += saw[i] - 1

    return ans

arr = [-778277028, -509675834, -828663475, 190114564, -34919218, -34919218, 106447210, -887980502, -399561546, -319453881, 564702467, -512179848, 634452898, -279371457, -279371457, -72310717, -770556513, -629539596, 112073567]
new_arr = [-442024811, 447425003, 365210904, 823944047, 943356091, -7819949958, 872885721, -296856571, 230380705, 944396167, -636263320, -942060800, -116260950, -126531946, -838921202]
print(countSawSubarrays(new_arr))


