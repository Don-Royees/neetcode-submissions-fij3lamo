class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = set(numbers)
        for i in range(len(numbers)):
            remaining = target - numbers[i]
            if remaining in n:
                if numbers.count(numbers[i]) > 1 :
                    return [i+1,numbers.index(remaining)+2]
                return [i+1,numbers.index(remaining)+1]       
        return []