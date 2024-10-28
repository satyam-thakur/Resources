import paramiko
import smtplib
from email.mime.text import MIMEText

# Configuration
filename = 'ip_address.txt'  # File containing the list of hosts
username = 'your_username'
password = 'your_password'
process_name = 'your_process_name'
report_email = 'your_email@example.com'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_user = 'your_smtp_username'
smtp_pass = 'your_smtp_password'

def load_hosts(filename):
    """Load hosts from a file."""
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def check_process(host):
    """Connect to a host and check for the specific process."""
    try:
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)
            command = f"pgrep -l {process_name} || echo 'Process not found'"
            stdin, stdout, stderr = ssh.exec_command(command)
            return f"{host}: {stdout.read().decode().strip()}"
    except Exception as e:
        return f"{host}: Error - {e}"

def send_email(report):
    """Send an email with the report."""
    msg = MIMEText(report)
    msg['From'] = smtp_user
    msg['To'] = report_email
    msg['Subject'] = 'Process Check Report'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

def main():
    hosts = load_hosts(filename)
    report = "\n".join(check_process(host) for host in hosts)
    send_email(report)
    print("Report sent!")

if __name__ == '__main__':
    main()
