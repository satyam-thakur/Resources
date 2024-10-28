#Palaindrome
class solution:
    def isPalindrome(self,s: str) -> bool:
        #store the character with alphanum in variable
        s = s.lower()
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        #compare the variable with the reverse of given string
        return new_s==new_s[::-1]

print(solution.isPalindrome(None,"tab a cat"))
