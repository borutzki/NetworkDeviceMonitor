import socket
import sys

def check_ssh(host):
    '''
    This function tries to port 22 of host. It returns 0 if connected or -1 if not. 
    '''
    try:
        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = Socket.connect_ex((host, 22))
        if result == 0:
            sys.stdout.write(f"Host {host} allows you to log in with SSH")
            return 0
        else:
            sys.stdout.write(f"Host {host} does not have the SSH port open")
            return -1
    except socket.gaierror:
        sys.stdout.write("Incorrect host name")
        return -2
    except:
        sys.stdout.write("Other error")
        return -4