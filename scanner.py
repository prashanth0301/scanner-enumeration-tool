import socket

from colorama import Fore, Style

from config import DEFAULT_TIMEOUT, COMMON_PORTS
from services import get_service
from banner import grab_banner

def scan_port(target,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(DEFAULT_TIMEOUT)
    result=sock.connect_ex((target,port))
    sock.close()
    return result==0

def enumerate_port(target,port):
    if not scan_port(target,port):
        return None
    service = get_service(port)
    banner = grab_banner(target,port)
    return {
        "port": port,
        "service": service["name"],
        "protocol": service["protocol"],
        "banner": banner
    }

def scan_target(target):

    scan_results = []

    print()

    for port in COMMON_PORTS:

        print(f"{Fore.CYAN}[+] Checking Port {port:<5}", end=" ")

        result = enumerate_port(target, port)

        if result:

            print(f"{Fore.GREEN}[OPEN]")

            scan_results.append(result)

        else:

            print(f"{Fore.RED}[CLOSED]")

    return scan_results