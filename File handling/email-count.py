import re

def count_email_addresses(filename):
    # Regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Dictionary to store email addresses and their counts
    email_counts = {}
    
    # Read the file and count email addresses
    with open(filename, 'r') as file:
        for line in file:
            # Find all email addresses in the line
            emails = re.findall(email_pattern, line)
            
            # Update the count for each email address
            for email in emails:
                email_counts[email] = email_counts.get(email, 0) + 1
    
    return email_counts

# Example usage
filename = 'input.txt'
result = count_email_addresses(filename)

# Print the results
print("Email address counts:")
for email, count in result.items():
    print(f"{email}: {count}")