class Solution:
    
        
    def twoSum(self,nums, target):
        dict={}
        for i in range(len(nums)):
            if target-nums[i] in dict.keys():
                return[dict[target-nums[i]], i]
            dict[nums[i]]=i
        
