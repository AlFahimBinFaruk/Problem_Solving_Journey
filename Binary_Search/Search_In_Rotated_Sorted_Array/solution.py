# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Time O(log(N)) | Space O(1)
def search(nums, target):
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = (l+r)//2

        if target == nums[mid]:
            return mid

        # Search left partition
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid+1
            else:
                r = mid-1
        # search right partition
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid-1
            else:
                l = mid+1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
