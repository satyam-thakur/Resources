filename = "ip_address.txt"

def load_host(file):
    with open(file,'r') as f:
        for ip in f:
            if ip.strip():
                print (ip)
                return [ip.strip()]
            else:
                continue
        # for ip in f:
        #     if ip.strip():
        #         print (ip)
        return [ip.strip() for ip in f if ip.strip()]
    
print (load_host(filename))