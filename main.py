#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NetArmor Security Suite
# dev: https://github.com/alidagdelen

import os
import sys

# ansi colors
class Colors:
    HEADER    = '\033[95m'
    BLUE      = '\033[94m'
    CYAN      = '\033[96m'
    GREEN     = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


def check_root():
    # root check for raw socket operations
    if os.geteuid() != 0:
        print(f"{Colors.FAIL}[!] ERROR: NetArmor requires root access!{Colors.ENDC}")
        print(f"{Colors.WARNING}[*] Try running: sudo python3 main.py{Colors.ENDC}")
        sys.exit(1)

def show_banner():
    # clear terminal screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(f"""{Colors.CYAN}{Colors.BOLD}
  _  _ _____ _____    _ ___ __  __  ___  ___ 
 | \| | __|_   _/_\  | | _ \  \/  |/ _ \| _ \\
 | .` | _|  | |/ _ \ | |   / |\/| | (_) |   /
 |_|\_|___| |_/_/ \_\|_|_|_\_|  |_|\___/|_|_\\
{Colors.ENDC}
{Colors.BLUE}================================================================={Colors.ENDC}
{Colors.BOLD} [>] Tool     :{Colors.ENDC} NetArmor v1.0 - All-in-One Security Tool
{Colors.BOLD} [>] Github   :{Colors.ENDC} {Colors.UNDERLINE}https://github.com/alidagdelen{Colors.ENDC}
{Colors.BLUE}================================================================={Colors.ENDC}
""")

def start_netrecon():
    try:
        from core import netracon
        print(f"\n{Colors.BLUE}[*] Launching NetRecon engine...{Colors.ENDC}\n")
        netracon.main()
    except ImportError:
        print(f"{Colors.FAIL}[-] Couldn't find 'netracon.py' inside core/ directory!{Colors.ENDC}")
    except Exception as err:
        print(f"{Colors.FAIL}[-] Error while running NetRecon: {err}{Colors.ENDC}")

def start_pathhunt():
    try:
        from core import pathHunt
        print(f"\n{Colors.BLUE}[*] Starting PathHunt tool...{Colors.ENDC}\n")
        pathHunt.main_menu()
    except ImportError:
        print(f"{Colors.FAIL}[-] File 'pathHunt.py' missing inside core/ directory!{Colors.ENDC}")
    except Exception as err:
        print(f"{Colors.FAIL}[-] PathHunt crash error: {err}{Colors.ENDC}")

def start_secsentinel():
    try:
        from core import SecSentinel
        print(f"\n{Colors.BLUE}[*] Starting SecSentinel monitor...{Colors.ENDC}\n")
        SecSentinel.main()
    except ImportError:
        print(f"{Colors.FAIL}[-] 'SecSentinel.py' file not found inside core/ directory.{Colors.ENDC}")
    except Exception as err:
        print(f"{Colors.FAIL}[-] Error in SecSentinel: {err}{Colors.ENDC}")

def main():
    check_root()
    
    while True:
        show_banner()
        print(f"{Colors.HEADER}--- MODULE SELECTION ---{Colors.ENDC}")
        print(f"{Colors.GREEN}[1]{Colors.ENDC} NetRecon    -> Network Discovery, Port Scan, MITM & DNS Tracker")
        print(f"{Colors.GREEN}[2]{Colors.ENDC} PathHunt    -> File Content Search & FIM Engine")
        print(f"{Colors.GREEN}[3]{Colors.ENDC} SecSentinel -> ARP Anomaly & Spoofing Detection System")
        print(f"{Colors.FAIL}[0]{Colors.ENDC} Exit\n")
        
        user_choice = input(f"{Colors.WARNING}NetArmor > {Colors.ENDC}").strip()
        
        if user_choice == "1":
            start_netrecon()
            input(f"\n{Colors.CYAN}Press Enter to return main menu...{Colors.ENDC}")
        elif user_choice == "2":
            start_pathhunt()
            input(f"\n{Colors.CYAN}Press Enter to return main menu...{Colors.ENDC}")
        elif user_choice == "3":
            start_secsentinel()
            input(f"\n{Colors.CYAN}Press Enter to return main menu...{Colors.ENDC}")
        elif user_choice == "0":
            print(f"\n{Colors.FAIL}[*] Exiting NetArmor... Stay safe!{Colors.ENDC}\n")
            sys.exit(0)
        else:
            print(f"\n{Colors.FAIL}[-] Invalid choice! Select valid option from menu.{Colors.ENDC}")
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.ENDC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}[*] Cancelled by user.{Colors.ENDC}")
        sys.exit(0)