#!/usr/bin/env python3

import argparse
import requests
import concurrent.futures

def print_red(text):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(RED + text + RESET)

def banner():
    banner = """

██████╗░██╗██████╗░██████╗░██╗░░░░░░█████╗░██████╗░███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
██║░░██║██║██████╔╝██████╦╝██║░░░░░███████║██║░░██║█████╗░░
██║░░██║██║██╔══██╗██╔══██╗██║░░░░░██╔══██║██║░░██║██╔══╝░░
██████╔╝██║██║░░██║██████╦╝███████╗██║░░██║██████╔╝███████╗
╚═════╝░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝      
    """
    print(banner)
    print_red("                                               by M1dn1ght-Zain")

if __name__ == "__main__":
    banner()
    print("")
    
def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

def dir_bruteforce(target_url, wordlist_path):
    with open(wordlist_path, 'r') as wordlist_file:
        for line in wordlist_file:
            directory = line.strip()
            test_url = f"{target_url}/{directory}"
            response = request(test_url)
            if response:
                print("[+] Discovered Directory ----->", test_url)

def main():
    parser = argparse.ArgumentParser(description="DirBlade - A directory bruteforcing tool")
    parser.add_argument("-u", "--url", help="Target URL (ex. http://example.com)", required=True)
    parser.add_argument("-w", "--wordlist", help="Path of the wordlist", default="default.txt")
    args = parser.parse_args()

    target_url = args.url
    wordlist_path = args.wordlist

    print("Target URL:", target_url)
    print("Wordlist:", wordlist_path)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda directory: dir_bruteforce(target_url, wordlist_path), range(1))

if __name__ == "__main__":
    main()
