def maxSubarraySumCircular(nums):
    def kadane(arr):
        current_sum = max_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    max_kadane = kadane(nums)
    max_wrap = sum(nums) - kadane([-x for x in nums])
    
    return max(max_kadane, max_wrap)

# Example usage:
nums = [1, -2, 3, -2]
print(maxSubarraySumCircular(nums))  # Output: 3
