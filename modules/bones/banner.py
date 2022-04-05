from pyfiglet import Figlet
from termcolor import colored

# Banner
dona = """
      ===================== Made by BraiNiac ==================
      ===================== Buy me a beer :) ==================
      ==== BTC: bc1q8z64uky7jgwdsygc7fwq97d4u8yfr8hj57s200 ====
      =========================================================
"""


def banner():
    f = Figlet(font='alligator')

    print(colored(f.renderText(' N u k e'), 'yellow'))
    print(colored(f.renderText('       T o w n'), 'green'))

    return print(dona)


banner()
