class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1 
        while left < right:
            if not (96< ord(s[left].lower()) < 123 or 47 < ord(s[left].lower()) < 58 ):
                left +=1
            elif not (96< ord(s[right].lower()) < 123 or 47 < ord(s[right].lower()) < 58  ):
                  right -= 1
            elif s[left].lower() != s[right].lower() :
                print(s[left],s[right])
                return False
            elif s[left].lower() == s[right].lower():
                left +=1
                right -=1
        return True         
