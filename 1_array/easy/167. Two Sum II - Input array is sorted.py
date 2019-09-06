# iterate through numbers, and use a dic to keep the index (key: target-item, value: index) 
# return both index if find the match key and number
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return False
        
        dic = {}
        for i, item in enumerate(numbers):
            if item in dic:
                return [dic[item], i+1]
            else:
                dic[target-item] = i+1
        return False