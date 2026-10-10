class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_duplicate = False
        if len(nums) != len(set(nums)):
            is_duplicate = True 

            
        return is_duplicate            