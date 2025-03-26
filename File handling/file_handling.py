ip_address = []
with open ("ntp_server.log", "r") as log:
    lines = log.readlines()
    print(log)
    for line in lines:
        if "Received" in line:
            words = line.split("(")
            print(line)
            # print(words)
            ip_add = words[1].split(")")
            # print(ip_add)
            ip_add = ip_add[0].split(",")
            # print(ip_add)
            print(ip_add[0].replace("'",""))
            ip_add = ip_add[0].strip("'")
            # print(ip_add)
            ip_address.append(ip_add)
    
print(ip_address)

with open("ip_address.txt", "w") as ip:
    for ips in ip_address:
        ip.writelines(ips+"\n")




