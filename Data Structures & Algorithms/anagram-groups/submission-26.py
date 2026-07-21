class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_array = []
        for i in strs:
            word = sorted(list(i)) 
            temp =[]
            for x in range(len(strs)):
                if word == sorted(list(strs[x])):
                    temp.append(strs[x])
            if temp not in return_array:        
                return_array.append(temp)        
        return return_array