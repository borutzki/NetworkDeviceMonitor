#!/usr/bin/env python

import argparse
from scripts.ping import ping
from scripts.check_ssh import check_ssh
from scripts.open_ports import open_ports
from scripts.ping_port import ping_port


def parse_arguments():
    '''
    This function defines arguments for argparse. Thanks to it, user can use command line.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument("host", metavar="H", type=str, help="host address")
    parser.add_argument("port",metavar="P",type=int, nargs="?", default=0, help="port number")


    parser.add_argument("--ping", help="Checks if host responds to ping")
    parser.add_argument("--pingport", help="Checks if host responds to ping on chosen port")
    parser.add_argument("--openports", help="Checks out a list of open ports on host")
    parser.add_argument("--ssh", help="Checks if you can log in to host with SSH ")

    args = parser.parse_args()

    return args

def main():
    '''
    This is main function. It takes argument from argparse and returns response code.
    '''
    if args.ping:
        res = ping(args.host)
    elif args.pingport:
        res = ping_port(args.host,args.port)
    elif args.openports:
        res = open_ports(args.host)
    elif args.ssh:
        res = check_ssh(args.host)
    return res


if __name__ == "__main__":
    args = parse_arguments()
    main()
