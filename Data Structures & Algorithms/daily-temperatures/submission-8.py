class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temprature , index 
        output = [0] * len(temperatures) #make an empty list with 0 filled  
        for index , i in enumerate(temperatures) : 
            while stack and stack[-1][0] < i:
                    num , pos = stack.pop()
                    output[pos] = index - pos 
            stack.append((i,index))
        return output               
 