

def can_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        sub_target = target - num
        res = can_sum(sub_target, nums, memo)
        if res:
            memo[target] = True
            return True

    memo[target] = False
    return False


def how_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums:
        sub_target = target - num
        sub_target_res = how_sum(sub_target, nums, memo)
        if sub_target_res is not None:
            sub_target_res.append(num)
            memo[target] = sub_target_res
            return memo[target]

    memo[target] = None
    return None


def coin_change_dp(amount, coins, memo={}):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    res = -1
    for coin in coins:
        remainder = amount - coin
        rem_res = coin_change_dp(remainder, coins, memo)
        if rem_res >= 0:
            rem_res += 1
            if res == -1 or rem_res < res:
                res = rem_res
    memo[amount] = res
    return res


def best_sum(target, nums, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    res = None
    for num in nums:
        rem = target - num
        rem_res = best_sum(rem, nums, memo)
        if rem_res is not None:
            rem_res = rem_res + [num]
            if (res is None) or (len(rem_res) < len(res)):
                res = rem_res

    memo[target] = res
    return res


# print(best_sum(100, [25, 2, 5]))


def valley_array(nums, target):

    res = 0

    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        check = 0 < m < len(nums) - 1
        if check and (nums[m-1] > nums[m] < nums[m+1]):
            bottom_i = m
        elif r-l <= 1:
            bottom_i = l
        if nums[m-1] < nums[m]:
            r = m-1
        else:
            l = m+1


    l, r = 0, bottom_i
    while l <= r:
        m = (l+r)//2
        if nums[m] < target < nums[m - 1]:
            res += m
        if nums[m] > target:
            l = m+1
        else:
            r = m-1

    l, r = bottom_i, len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m] < target < nums[m+1]:
            res += len(nums) - m - 1
        if nums[m] > target:
            r = m-1
        else:
            l = m+1

    return res


arr = [19, 17, 15, 12, 7, 5, 3, 4, 8, 14, 22]
target = 6
# print(valley_array(arr, target))


def merge(left, right):
    i, j, k = 0, 0, 0
    res = [0]*(len(left) + len(right))
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1
    while i<len(left):
        res[k] = left[i]
        i += 1
        k += 1
    while j<len(right):
        res[k] = right[j]
        j += 1
        k += 1
    return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = (len(arr)-1)//2
    left = arr[0:m+1]
    right = arr[m+1:len(arr)]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)



# nums = [1, 5, 2, 4, 5, 9, 1, 0, 2, 4]
# print(merge_sort(nums))


def l2_dist(point):
    print(point[0] ** 2 + point[1] ** 2)
    return (point[0] ** 2 + point[1] ** 2)


def merge_(left, right):
    res = [0]*(len(left)+len(right))
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if l2_dist(left[i]) < l2_dist(right[j]):
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        res[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        res[k] = right[j]
        k += 1
        j += 1
    return res

print(merge_([[2,3]], [[1,0]]))

from collections import OrderedDict

