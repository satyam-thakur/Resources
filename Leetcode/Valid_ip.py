def is_valid_ipv4(ip):
    parts = ip.split('.')
    #Check if lenth of decimal points are 4
    if len(parts) != 4:
        return False
    
    for part in parts:
        #Check if each part is digit and with in range 0-255
        if not part.isdigit() and not 0<= int[part] <=255:
            return False
        #Checks for any leading Zero, except '0' itself
        if part != '0' and part[0] == '0':
            return False
    return True

print(is_valid_ipv4("192.168.0.1"))
print(is_valid_ipv4("092.168.0.1"))

