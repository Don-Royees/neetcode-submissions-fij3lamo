class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        dic = {")":"(","}":"{","]":"["}
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            elif not stack :
                return False
            elif stack[-1] == dic[i] :
                stack.pop()
            else:
                return False    
        return len(stack)==0               