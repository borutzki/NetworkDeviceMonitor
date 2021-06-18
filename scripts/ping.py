import subprocess
import sys

def ping(host):
    '''
    This function checks out if host responds to ping. It returns 0 if host responds or -1 if it does not respond.
    '''
    res = subprocess.call("ping -n 1 " + host)
    if res == 0:
        sys.stdout.write(f"Host {host} responded to ping!")
        return 0
    else:
        sys.stdout.write("Server does not respond to ping")
        return -1