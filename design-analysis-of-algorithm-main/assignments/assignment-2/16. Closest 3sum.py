def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
                
    return closest_sum

nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))