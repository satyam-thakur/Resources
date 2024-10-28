#Import the python library 
import paramiko
import smtplib
from email.mime.text import MIMEText

# Initailaze the necessary variables with input
filename = 'ip_address.txt'
username = 'u2000'
password = 'Test@123'
smtp_server = "server ip address"
smtp_user = "smtp user"
smtp_pass = "smtp password"
smpt_port = 587
report_mail = "mail to report"
process_name = "process_name"

#Read the hosts file
def load_host(file):
    with open(file,'r') as f:
        for ip in f:
            if ip.strip():
                print (ip)
                return [ip.strip()]
            else:
                continue

#Define the function: to connect to hosts and execute command
def check_process(host):
    with paramiko.SSHClient() as ssh:
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect (host, username=username, password=password)
            command = f"pgrep -l {process_name} || echo 'Process not found'"
            stdin,stdout,stderr = ssh.exec_command(command)
            return [f"{host}:{stdout.read().decode().strip()}"]
        except Exception as e:
            return [f"{host}: Error -{e}"] 

#Define the Function: To send report mail
def send_mail(report):
    msg = MIMEText(report)
    msg['From'] : smtp_user
    msg['To'] : report_mail
    msg['Subject'] : "Process reports"

    with smtplib.SMTP(smtp_server, smpt_port) as server:
        try:
            server.starttls()
            server.login(smtp_user,smtp_pass)
            server.send_message(msg)
        except Exception as e:
            return [f"failed to send mail : Error- {e}"]

#Define main function:
def main():
    hosts = load_host(filename)
    report = "/n".join(check_process(host) for host in hosts)
    print (send_mail(report))

# program start point
if '__name__' == '__main__':
    main()
