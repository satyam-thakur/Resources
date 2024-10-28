import paramiko
import smtplib
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
HOSTS_FILE = 'ip_address'
USERNAME = 'your_username'
PASSWORD = 'your_password'
PROCESS_NAME = 'your_process_name'
REPORT_EMAIL = 'your_email@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'your_smtp_username'
SMTP_PASS = 'your_smtp_password'
MAX_WORKERS = 10  # Number of concurrent connections

def load_hosts(filename):
    """Load hosts from a file."""
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def check_process(host):
    """Connect to a host and check for the specific process."""
    try:
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=USERNAME, password=PASSWORD, timeout=10)
            command = f"pgrep -l {PROCESS_NAME} || echo 'Process not found'"
            stdin, stdout, stderr = ssh.exec_command(command)
            return f"{host}: {stdout.read().decode().strip()}"
    except Exception as e:
        return f"{host}: Error - {str(e)}"

def send_email(report):
    """Send an email with the report."""
    msg = MIMEText(report)
    msg['From'] = SMTP_USER
    msg['To'] = REPORT_EMAIL
    msg['Subject'] = 'Process Check Report'

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def main():
    hosts = load_hosts(HOSTS_FILE)
    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_host = {executor.submit(check_process, host): host for host in hosts}
        for future in as_completed(future_to_host):
            results.append(future.result())

    report = "\n".join(results)
    send_email(report)

if __name__ == '__main__':
    main()