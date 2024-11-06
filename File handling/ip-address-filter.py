ip_address = []
with open('ntp_server.log', 'r') as log:
    lines = log.readlines()
    for line in lines:
        if 'Received' in line:
            ip = line.split('(')
            ip = ip[1].split[',']
            ip = ip[0].strip(',')
            ip = ip[0]
            print (ip)
            ip_address.append(ip)


with open('ip-addresses.txt', 'w') as file:
    for ip in ip_address:
        ip.writelines(ip+"\n")
        
