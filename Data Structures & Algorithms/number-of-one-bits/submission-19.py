class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        print(str(bin(n)))
        n = list(str(bin(n)))
        for i in n:
            if i == "1":
                count = count + 1
        return count          