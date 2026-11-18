def maxProfit(nums):
    max = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            m = nums[j] - nums[i]
            if m > max:
                max = m
    return max

def maxProfit2(nums):
    mini = nums[0]
    maxp = 0
    for i in range(len(nums)):
        if nums[i] < mini:
            mini = nums[i]

        p = nums[i] - mini

        if p > maxp:
            maxp = p

    return maxp

prices = [7, 1, 5, 3, 6, 4, 7]
print(maxProfit2(prices))
        