class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for i in s :
            if ord(i)<65 or ord(i)>122 or 91<=ord(i)<=96: 
                if i in "1234567890":
                    ns+=i
                else:
                    continue
            else :
                if ord(i)>90 :
                    i = chr(ord(i)-32)
                    ns+=i
                else :
                    ns+=i
        return ns == ns[::-1]