class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for t in tokens:
            if t == "+":
                a ,b = stack.pop() , stack.pop()
                stack.append(a+b)
            elif t == "-":
                a ,b = stack.pop() , stack.pop()
                stack.append(b - a)  
            elif t == "/":
                a ,b = stack.pop() , stack.pop()
                print(a,b)
                stack.append(int(float(b) / a)) 
            elif t == "*":
                a ,b = stack.pop() , stack.pop()
                stack.append(a * b) 
            elif t not in "*/-+":
                stack.append(int(t))
        return stack[0]       
