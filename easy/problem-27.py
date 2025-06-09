class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        sorted_list=[]
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
            else:
                sorted_list.append(nums[i])
        while "_" in nums:
            nums.remove("_")
        return len(sorted_list)
        
        
        