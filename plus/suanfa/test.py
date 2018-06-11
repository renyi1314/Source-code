a = [2, 7, 11, 15]
b = 9


def twosum(nums, target):
    for i in range(len(nums)):
        tmp = list(range(len(nums)))
        tmp.remove(i)
        for j in tmp:
            if nums[i] + nums[j] == target:
                return [i, j]


print(twosum(a, b))
