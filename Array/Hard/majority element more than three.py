def majorityElement(nums):
    if not nums:
        return []

    # 1st pass: Find potential candidates
    count1 = count2 = 0
    candidate1 = candidate2 = None

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # 2nd pass: Verify counts
    result = []
    n = len(nums)
    if nums.count(candidate1) > n // 3:
        result.append(candidate1)
    if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
        result.append(candidate2)

    return result
print(majorityElement([3, 2, 3]))            # Output: [3]
print(majorityElement([1,1,1,3,3,2,2,2]))    # Output: [1, 2]
