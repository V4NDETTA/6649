import uuid
import time
import requests
from colorama import init, Fore, Style
from lcu_driver import Connector
import aiohttp
import asyncio
import subprocess


# Initialize colorama
init(autoreset=True)

def print_header():
    print(Fore.RED + Style.BRIGHT + "WE CLIMB TOGETHER 1.0" + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "Send Device ID to Dev to Get Activated !" + Style.RESET_ALL)
    print("Please Wait...")
    print_loading_effect()
    print("v1.0")
    print("\n\n")

def encrypt_device_id(device_id):
    # Simple XOR encryption example, you can replace this with a more secure method
    key = 0x42  # Replace with your own key
    encrypted_id = ''.join([chr(ord(char) ^ key) for char in device_id])
    return encrypted_id

def get_short_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    short_mac = '.'.join([str(int(pair, 16)) for pair in mac.split(':')])
    return short_mac

def generate_random_encrypted_mac():
    # Generate a random string of uppercase letters and digits, length between 10 and 15
    import random
    import string
    length = random.randint(10, 15)
    encrypted_mac = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)).upper()
    return encrypted_mac

def check_mac_in_raw_file(encrypted_mac_address, raw_link):
    response = requests.get(raw_link)
    if response.status_code == 200:
        keys = response.text.split('\n')
        return encrypted_mac_address in keys
    else:
        print(f"Failed to fetch keys. Status code: {response.status_code}")
        return False

def authenticate_user(mac_address, raw_link):
    encrypted_mac_address = encrypt_device_id(mac_address)

    print(Fore.YELLOW + Style.BRIGHT + "Device ID:", encrypted_mac_address + Style.RESET_ALL)
    print("")

    if check_mac_in_raw_file(encrypted_mac_address, raw_link):
        print(Fore.GREEN + Style.BRIGHT + "Please wait, enabling tool..." + Style.RESET_ALL)
        time.sleep(3)
        return True
    else:
        print(Fore.RED + Style.BRIGHT + "Your Device ID is Not Activated!" + Style.RESET_ALL)
        user_input = input("Enter 'yes' to exit ")
        return False

def get_patch_url_from_raw_link(raw_link):
    response = requests.get(raw_link)
    if response.status_code == 200:
        patch_url = response.text.strip()
        return patch_url
    else:
        print(f"Failed to fetch patch URL from raw link. Status code: {response.status_code}")
        return None

def main():
    print_header()
    # DEVICE ID ( RAW ONLY )
    raw_link = "https://pastebin.com/raw/UN9Y8D6S"
    mac_address = get_short_mac_address()

    print("\n")

    # Your authentication check
    if authenticate_user(mac_address, raw_link):
        print(Fore.CYAN + Style.BRIGHT + "Tool Enabled. Check the LeagueClient." + Style.RESET_ALL)
        print("")
        print("")
        print("────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌")
        print("───▄▄██▌█ BEEP BEEP")
        print("▄▄▄▌▐██▌█ +40 LP DELIVERY")
        print("███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌")
        print("▀(⊙)▀▀▀▀▀▀▀(⊙)(⊙)▀▀▀▀▀▀▀▀▀▀(⊙)")

        # Run omen.py using subprocess
        subprocess.run(['python', 'omen.py'])

        exit_choice = input(Fore.YELLOW + Style.BRIGHT + "Press Enter to exit." + Style.RESET_ALL)
        if exit_choice.lower() == 'exit':
            exit()
    else:
        exit_choice = input(Fore.YELLOW + Style.BRIGHT + "Press Enter to exit." + Style.RESET_ALL)
        if exit_choice.lower() == 'exit':
            exit()


def print_loading_effect():
    print(Fore.YELLOW + Style.BRIGHT + "Loading", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)  # Adjust the sleep duration for the desired speed
        print(".", end="", flush=True)
    print(Style.RESET_ALL)  # Reset color after the loading effect

if __name__ == "__main__":
    main()

exit_choice = input(Fore.YELLOW + Style.BRIGHT + "Press Enter to exit." + Style.RESET_ALL)
