class Solution:
    def reverseBits(self, n: int) -> int:
        n= bin(n).split("b")[1][::-1]
        num = "0b"
        for i in n:
            num = num + i 
        for x in range(32-len(n)):
            num = num + "0"    
        print(num)
        return int(num, 2
        )    
