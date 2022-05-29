#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
    found_ports = []

    while min_port <= max_port :
        s = socket.socket()
        print ("Tentative de connection :  ", min_port)
        try :
            s.connect((address, min_port))
            data = s.recv(1024)
            print ("Connection réalisée :  ", min_port)
            found_ports.append(min_port)
            min_port = min_port + 1
            break
        except  :
            print("Error : no response")
            min_port = min_port + 1


    return found_ports


def main(argv):
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = get_accessible_ports(address, min_port, max_port)
    for p in ports:
        print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('usage: python %s address min_port max_port' % sys.argv[0])
    else:
        main(sys.argv)