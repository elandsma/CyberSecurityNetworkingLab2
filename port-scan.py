#!/user/bin/env python3
'''
Elias Landsman
April 5, 2020
CSCI373 Networking Lab 2
'''

import socket
import os

host = "montreat.cs.unca.edu"

def main():
    ret_val = os.system("ping -c 1 -W 1 {0} > /dev/null".format(host))
    if(ret_val==0):
        print(f"ping: {format(host)} is up")
    else:
        print(f"Could not ping {format(host)}")
        return
    ports = range(1,1023)
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
            print(f"\tOSError on port {format(port)}: {e}")

if __name__=='__main__':
    main()
