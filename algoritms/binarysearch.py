def binarysearch(ls, target):
    a = 0
    b = len(ls) - 1
    while a <= b:
        avg = (a + b) // 2
        if (ls[avg] == target):
            return avg
        elif target > ls[avg]:
            a = avg + 1
        else:
            b = avg - 1
    return -1
    

nums = [-1, 0, 3, 5, 9, 12]
target = 12
print(binarysearch(nums, target))