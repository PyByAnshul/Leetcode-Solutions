class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            relate_dic = {i:abs(target - i) for i in nums}
            min_keys = dict(sorted(relate_dic.items(), key=lambda item : item[1]))
            for min_key in min_keys:
                if min_key < target:
                    indx=nums.index(min_key)      
                    nums.insert(indx+1,target)
                    break
            else:
                nums.insert(0,target)
            return self.searchInsert(nums,target)
                
        
a= Solution()
print(a.searchInsert([1,3,5,6]
,0))