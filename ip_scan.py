import socket
import sys
IP = input("Enter a remote IP to scan: ")
print ("Please wait, scanning remote IP", IP)
try:
    for port in range(1,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP, port))
        if result == 0:
         print ("Port: ",port," 	 Open")
        sock.close()
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()
except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

