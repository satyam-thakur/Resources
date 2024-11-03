from bs4 import BeautifulSoup
import re
import csv

def extract_emails_to_csv(html_file, csv_file):
    # Step 1: Read the HTML content
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Step 2: Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()  # Extract only the text part of the HTML
    
    # Step 3: Extract valid email addresses using regex
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    
    # Remove duplicate emails (optional)
    emails = list(set(emails))
    
    # Step 4: Write emails to a CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Email Address'])  # Write header
        for email in emails:
            writer.writerow([email])

# Example usage
extract_emails_to_csv('example.html', 'emails.csv')
