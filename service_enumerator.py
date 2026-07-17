import socket
import datetime
from colorama import Fore, Style


from scanner import scan_target
from utils import display_banner, separator
from config import PROGRAM_NAME, VERSION, RESULT_FILE
def validate_target(target):
     try:
           socket.gethostbyname(target)
           return True
     except socket.gaierror:
           return False
     
def save_results(target,results):
    with open(RESULT_FILE,'a') as file:
        file.write("=" * 60 + "\n")
        file.write(f"Target : {target}\n")
        file.write(f"Scan Time : {datetime.datetime.now()}\n\n")
        for result in results:
            file.write(f"Port : {result['port']}\n")
            file.write(f"Service : {result['service']}\n")
            file.write(f"Protocol : {result['protocol']}\n")
            file.write(f"Banner : {result['banner']}\n")
            file.write("-" * 60 + "\n")
def main():

    display_banner()

    target = input("Enter Target IP or Hostname: ").strip()

    if not validate_target(target):
        print("\n[-] Invalid target.")
        return

    separator()

    print("[+] Starting Service Enumeration...\n")

    results = scan_target(target)

    if not results:
        print("[-] No open services found.")
        return

    separator()

    print(
        f"{'PORT':<8}"
        f"{'SERVICE':<18}"
        f"{'PROTOCOL':<10}"
        f"BANNER"
    )

    separator()

    for result in results:

        banner = result["banner"].splitlines()[0]

        if len(banner) > 45:
            banner = banner[:45] + "..."

        print(
            f"{Fore.GREEN}{result['port']:<8}"
            f"{Fore.YELLOW}{result['service']:<18}"
            f"{Fore.CYAN}{result['protocol']:<10}"
            f"{Fore.WHITE}{banner}"
        )

    separator()

    print(f"Target            : {target}")
    print(f"Services Found    : {len(results)}")
    print(f"Results File      : {RESULT_FILE}")

    save_results(target, results)

    print("\n[+] Scan completed successfully.")
    
if __name__ == "__main__":
    main()