import sys
import os
import wget
from colorama import Fore

if os.name == 'nt':
    winpcap_url = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
    winpcap_dir = os.environ['ProgramFiles(x86)'] + '\\WinPcap'
    if not os.path.exists(winpcap_dir):
        print(
            f'{Fore.MAGENTA}[!] {Fore.YELLOW}"WinPcap" module is not installed.\n It is a necessary tool to perform several kinds of attacks,\n you may skip this step if you wish to perform SMS flooding only\n Continue WinPcap installation? (y/n){Fore.RESET}'
        )
        if input(
                f'{Fore.MAGENTA} ---> {Fore.BLUE}').lower() in ('y', 'yes'):
            print(
                f'{Fore.YELLOW}[~] {Fore.CYAN}Downloading installer...{Fore.BLUE}\n')
            winpcap_installer = wget.download(winpcap_url)
            os.startfile(winpcap_installer)
            print(
                f'\n\n{Fore.GREEN}[?] {Fore.YELLOW}Installation finished. Please restart program{Fore.RESET}'
            )
            sys.exit(1)
