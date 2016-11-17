# listens to socket for ping and lights block when heard

import time
import socket
import block

VERBOSE = False

def listen():
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)

    while True:
        data, addr = s.recvfrom(1508)
        if VERBOSE:
            print("Packet from %r: %r" % (addr,data))
        else:
            print("Pinged from ", addr)

        block.power_on()
        block.setlevel(3)
        time.sleep(1)
        block.power_off()

listen() 
