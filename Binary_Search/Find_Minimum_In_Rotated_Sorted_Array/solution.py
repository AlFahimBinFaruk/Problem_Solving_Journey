# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Time O(log(N)) | Space O(1)
def findMin(nums):
    result=nums[0]

    l=0
    r=len(nums)-1

    while l<=r:
        mid=(l+r)//2
        # if the array is sorted
        if nums[l]<nums[r]:
            result=min(result,nums[l])

        result = min(result,nums[mid])

        if nums[mid]>=nums[l]:
            l = mid+1
        else:
            r = mid-1

    return result

print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([3, 4, 5, 1, 2]))                  