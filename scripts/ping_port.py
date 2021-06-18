import socket
import sys

def ping_port(host, port):
    '''
    This function checks out if selected port of host responds to connection. It returns 0 if port responds or -1 if it does not respond.
    '''
    try:
        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = Socket.connect_ex((host, int(port)))
        sys.stdout.write(res)
        Socket.shutdown(2)
        if res == 0:
            sys.stdout.write(f"Connected to port {port} on host {host}")
            return 0
        elif res == 10060:
            sys.stdout.write(f"Port {port} on host {host} does not respond")
            return -1
    except socket.gaierror:
        sys.stdout.write("Incorrect host name")
        return -2
    except KeyboardInterrupt:
        sys.stdout.write("Testing port stopped by user")
        sys.exit()
        return -3
    except:
        sys.stdout.write("Other error")
        return -4