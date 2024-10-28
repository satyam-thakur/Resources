import socket
s = socket.socket()
'''initialize socket'''
port = 1234
s.bind(('', port))
s.listen(2)
while True:
    a, b = s.accept()
    print("request accepted from the address,",b)
    a.send("received your connection reuest thanks")
    a.close()
