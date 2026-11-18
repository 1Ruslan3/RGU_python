def twoSum(nums, target):
        dic = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if x in dic:
                return [dic[x], i]

            dic[nums[i]] = i

        return []

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))