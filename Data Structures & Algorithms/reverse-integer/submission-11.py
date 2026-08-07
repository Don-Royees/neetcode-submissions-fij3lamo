class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        n = False
        if abs(x) != x:
            num = num[1:len(num)]
            n=True
        num = num[::-1]    
        if n :
            num = "-" + num
        num = int(num)
        if num>2**31 -1 or num<-2**31:
            num = 0 
        return num
    