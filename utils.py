from colorama import Fore, Style, init

init(autoreset=True)


def display_banner():

    print(Fore.CYAN + "=" * 70)
    print(Fore.GREEN + Style.BRIGHT)

    print("           SERVICE ENUMERATION TOOL")
    print("        Red Team Reconnaissance")
    print("              Version 1.0")

    print(Fore.CYAN + "=" * 70)


def separator():

    print(Fore.CYAN + "-" * 70)