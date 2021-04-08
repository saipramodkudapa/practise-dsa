

def uniqueTwoSum(nums, target):
    comp, ans = set(), set()
    for num in nums:
        c = target - num
        if c in comp:
            res = (num, c) if num > c else (c, num)
            ans.add(res)
        comp.add(num)

    # ans will have unique pairs
    return len(ans)
