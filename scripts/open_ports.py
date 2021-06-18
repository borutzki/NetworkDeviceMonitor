import socket
import sys

def open_ports(host):
    '''
    This function takes host address and scans ports one by one. It lists open ones and returns an array of them.
    '''
    # UDP: 0 - 655355
    open_ports = []
    try:
        for port in range(0, 65535):
            Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = Socket.connect_ex((host, int(port)))
            if result == 0:
                print(f"Port {port} on host {host} is open")
                open_ports.append(port)
            Socket.close()
            
    except KeyboardInterrupt:
        sys.stdout.write("Scanning stopped by user")
        sys.exit()
        return -3
    except socket.gaierror:
        sys.stdout.write("Incorrect host name")
        return -2
    except:
        sys.stdout.write("Other error")
        return -4
    return open_ports