class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"[":"]" ,"{" : "}" , "(" : ")"}
        stack = []
        for i in s:
            if i in dic:
                item = dic[i]
                print(item)
                stack.append(item)
            else:
                if not stack or i != stack[-1]:
                    return False
                stack.pop()
        return not stack         