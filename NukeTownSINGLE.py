from scapy.all import *
import socket
import threading


target_ip = input('Enter targe IP address: ')
sourcee_ip = input("Enter source IP address: ")
# fake_ip = input('Enter fake IP address: ')
target_port = int(input('Enter target Port number: '))
source_port = int(input('Enter source Port number: '))
i = 1

while True:
    IP1 =
    IP(sourcee_ip = sourcee_ip, desination = target_ip)
    TCP1 = TCP(srcport = source_port, dstport = 80)
    pkt = IP1 / TCP1
    send(pkt, inter = .001)
    
    print('packeet sent ', i)
    i = i + 1
