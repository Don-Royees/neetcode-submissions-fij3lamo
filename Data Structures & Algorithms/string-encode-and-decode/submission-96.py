class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in strs:
            word = word + "#" + str(len(i)) + "#" + i  
        return word     
    def decode(self, s: str) -> List[str]:
        strs = []
        check = False
        length = ""
        count = 0
        while count < len(s):
            if check and s[count] != "#":
                length = length + s[count]
            if s[count] == "#":
                if not check:
                    check = True
                else:
                    check = False
            if not check and length != "":
                strs.append(s[count+1:count + int(length)+1])
                count = count + int(length)+1
                length = ""
                check = False
                continue
            elif check:   
                count = count + 1  
        return strs              



