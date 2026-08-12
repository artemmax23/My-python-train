def two_sum_sorted(nums: list, target: int) -> list:
    i  = 0
    j = len(nums) - 1
    while (nums[i] + nums[j]) != target:
        if (nums[j] > target) or ((nums[j] + nums[i]) >  target):
            j -= 1
        else:
            i += 1
        
    return sorted([i, j]) 
    
def two_sum(nums: list, target: int) -> list:
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
        
    return []
            
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))          # [0, 1]
print(two_sum([-3, -2, 3, 4], 2))  # [1, 3] (-2 + 4 = 2)