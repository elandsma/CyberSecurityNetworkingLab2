#!/user/bin/env python3


import socket
import os

host = "arden.cs.unca.edu"
ports = [21, 22, 53, 80, 443 ]
'''
22 - SSH
21 - FTP
25 - SMTP
53 - DNS
80 - HTTP
443 - HTTPS
'''
#todo: 0-1023

#todo: write output

def main():
    print("hello whirled")
    ret_val = os.system("ping -c 1 -w1 {0} > /dev/null".format(host))
    if(ret_val==0):
        print(f"ping {format(host)} is up")
    else:
        print(f"Could not ping {format(host)}")
        return

    for port in ports:
        try:
            print(f"Trying to connect to {format(host)} on port {format(port)}")
            sock = socket.create_connection((host, port), timeout=1)
            #if we get here, TCP connection made, therefore port is open.
            print(f"\tConnected to port {format(port)}")
            sock.close()
        except socket.timeout as e:
            print(f"\tTimeout on port {format(port)}: {e}.")
        except ConnectionRefusedError as e:
            print(f"\tConnection refused on port {format(port)}: {e}")
        except OSError as e:
            print(f"\tOSError of port {format(port)}: {e}")

if __name__=='__main__':
    main()

