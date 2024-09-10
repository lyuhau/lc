
def threeSum(nums):
    nums = list(sorted(nums))
    result = set()
    for k, num in enumerate(nums):
        pairs = twoSum(nums, -num)
        for i, j in pairs:
            if len({i, j, k}) == 3:
                result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return list(result)


def twoSum(numbers, target):
    if not numbers:
        return []
    result = []
    i = 0
    j = len(numbers) - 1
    while i != j:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            result.append((i, j))
            i += 1
    return result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([]))
    print(threeSum([0]))
    # print(threeSum([0, 0, 0]))
    # print(threeSum([0, 0, 0, 0]))
    # print(threeSum([0, 0, 0, 0, 0]))
    # print(threeSum([0, 0, 0, 0, 0, 0]))
    # print(threeSum([0, 0, 0, 0, 0, 0, 0]))
    # print(threeSum([0, 0, 0, 0, 0, 0, 0, 0]))
    # print(threeSum([0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # print(threeSum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # print(threeSum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
