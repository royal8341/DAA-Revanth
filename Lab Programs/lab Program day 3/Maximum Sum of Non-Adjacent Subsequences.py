def maxSumAfterQueries(nums, queries):
    def maxNonAdjacentSum(arr):
        incl = 0
        excl = 0
        for num in arr:
            new_excl = max(excl, incl)
            incl = excl + num
            excl = new_excl
        return max(incl, excl)
    
    total_sum = 0
    MOD = 10**9 + 7
    for pos, x in queries:
        nums[pos] = x
        total_sum += maxNonAdjacentSum(nums)
    return total_sum % MOD

# Example usage:
nums = [1, 2, 3, 4]
queries = [[1, 3], [2, 5]]
print(maxSumAfterQueries(nums, queries))  # Output will vary based on specific queries
