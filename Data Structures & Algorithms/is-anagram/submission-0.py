class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = []
        two = []
        for i in s:
            one.append(i)
        for i in t:
            two.append(i)
        
        if sorted(one) == sorted(two):
            return True
        else:
            return False 
    



        