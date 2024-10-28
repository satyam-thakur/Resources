def isValid(s: str) -> bool:
    # Initialize an empty stack to store opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the input string
    for char in s:
        # If the character is an opening bracket
        if char in brackets.values():
            # Push it onto the stack
            stack.append(char)
        
        # If the character is a closing bracket
        elif char in brackets:
            print (char)
            # Check if the stack is empty or the top doesn't match the corresponding opening bracket
            if not stack or stack.pop() != brackets[char]:
                # If either condition is true, the string is invalid
                return False
    
    # After processing all characters, check if the stack is empty
    # If it's empty, all brackets were matched; otherwise, some were left unopened
    return len(stack) == 0

print (isValid("(()){}{"))
