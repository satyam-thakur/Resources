def ispalaindrome(s:str) -> bool:
    s = s.lower()
    new_s=""
    for char in s:
        if char.isalnum():
            new_s+=char
    return new_s==new_s[::-1]

print(ispalaindrome('satasa'))