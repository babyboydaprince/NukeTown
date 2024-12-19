# Created by BraiNiac
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from modules.crash_handler import CriticalError
    import modules.bones.clear
    import modules.bones.banner
    import modules.bones.winpcap
    from modules.way import TestingMethod
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args
parser = argparse.ArgumentParser(description="Nuke Town - Performance and stress testing tollset")
parser.add_argument(
    "--target",
    type=str,
    metavar="<IP:PORT, URL, PHONE>",
    help="Target ip:port, url or phone",
)
parser.add_argument(
    "--way",
    type=str,
    metavar="<JACKPHONE/JACKMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>",
    help="Testing technique",
)
parser.add_argument(
    "--time", type=int, default=10, metavar="<time>", help="time in secounds"
)
parser.add_argument(
    "--threads", type=int, default=3,
    metavar="<threads>", help="threads count (1-200)"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
way = str(args.way).upper()
target = args.target


if __name__ == "__main__":
    # Print help
    if not way or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run test
    with TestingMethod(
        duration=time, name=way, threads=threads, target=target
    ) as burst_sender:
        burst_sender.Start()
