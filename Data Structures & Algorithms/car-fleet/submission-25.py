class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = list(zip(position , speed))
        pair.sort()
        for i in range(len(pair)-1 ,-1 , -1 ):
            time = (target - pair[i][0] )  / pair[i][1] 
            if stack:
                if stack[-1] < time:
                    stack.append(time)
            else :
                stack.append(time)    
        fleet = len(stack) 
        print(stack )
        return fleet     

