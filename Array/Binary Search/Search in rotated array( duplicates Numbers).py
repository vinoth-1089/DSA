### duplicates Numbers



def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] == nums[right]== nums[left]:
            left+=1
            right-=1
            continue
           

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
nums = [7,8,9,1,2,3,3,3,4,5,6]
target = 3
print(search_rotated_array(nums, target))  
