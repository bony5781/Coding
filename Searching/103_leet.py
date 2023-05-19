def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        if (nums[mid] == target):
            return mid
        elif nums[low] <= nums[mid]:
            if (nums[low] <= target and target <= nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (nums[mid] <= target and target <= nums[high]):
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2, 3]
print(search(nums, 3))
