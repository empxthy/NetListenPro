#! /usr/bin/python3

# Coding: UTF-8
# Name: TCP-Listener
# Author: AlexEmployed
# Version: 1.0.0
# License: GPL-3.0 version
# Copyright: alexemployed 2023
# Github: https://github.com/alexemployed
# Language: Python


# Imports
import sys
import os
import asyncio
import platform
import requests
import shutil
import subprocess

# Version
_version = "1.0.0"

# Colors
_black = "\033[0;30m"
_red = "\033[0;31m"
_green = "\033[0;32m"
_brown = "\033[0;33m"
_blue = "\033[0;34m"
_yellow = "\033[1;33m"
_purple = "\033[0;35m"
_cyan = "\033[0;36m"
_white="\033[0;37m"
_lightGray = "\033[0;37m"
_darkGray = "\033[1;30m"
_lightRed = "\033[1;31m"
_lightGreen = "\033[1;32m"
_lightBlue = "\033[1;34m"
_lightPurple = "\033[1;35m"
_lightCyan = "\033[1;36m"
_lightWhite = "\033[1;37m"

# Version
_version = "1.0.0"

# Check Update
def check_update(repo_owner, repo_name, current_version):
    print(f"{_yellow}[!]{_white}Checking for updates...")

    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        latest_release = response.json()
        latest_version = latest_release["tag_name"]

        if current_version >= latest_version:
            print(f"{_green}[+]{_white}Your software is up to date (version {current_version}).")
        else:
            print(f"{_red}[-]{_white}A new version ({latest_version}) is available. Please update your software.")
            upt = str(input(f"{_yellow}[!]{_white}Update now?: [{_green}y{_white}/{_red}n{_white}]\n{_yellow}[?]{_white}Y/N: "))
            clone_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            if upt == "y":
                try:
                    shutil.rmtree(clone_path)
                    subprocess.run(["git", "clone", "https://github.com/alexemployed/NetListenPro.git", clone_path], check=True)
                    print(f"{_green}[+]{_white}Repository cloned successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {_red}{e}{_white}")
            
            if upt == "n":
                print(f"{_red}[-]{_white}Update cancelled by user!")
                sys.exit(1)
    
    except requests.exceptions.RequestException as e:
        print(f"{_red}[-]{_white}Error: {e}")
        print(f"Response content: {response.content}")


# Privalages
os_name = platform.system()
    
def check_root():
    ret = 0
    if os.geteuid != 0:
        msg = "[sudo] password for %u: "
        ret = subprocess.check_call("sudo -v -p '%s'" %msg, shell=True)
    return ret

def check_admin():
    try:
        subprocess.check_call(["net", "session"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Functions
async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        print(f"{_green}[+]{_white} {_darkGray}{ip}{_white}:{_green}{port}{_white} is {_green}OPEN{_white}")
        log_txt = f"{host}:{port} is OPEN!\n"
        with open('logs.txt', 'a+') as file: 
            file.write(log_txt)
        
        writer.close()
    except:
        pass

async def scan_ports(ip):
    tasks = [scan_port(ip, port) for port in range(1, 1024)]
    await asyncio.gather(*tasks)

# Get the host from the user
print(f"""
███╗   ██╗███████╗████████╗██╗     ██╗███████╗████████╗███████╗███╗   ██╗██████╗ ██████╗  ██████╗ 
████╗  ██║██╔════╝╚══██╔══╝██║     ██║██╔════╝╚══██╔══╝██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔═══██╗
██╔██╗ ██║█████╗     ██║   ██║     ██║███████╗   ██║   █████╗  ██╔██╗ ██║██████╔╝██████╔╝██║   ██║
██║╚██╗██║██╔══╝     ██║   ██║     ██║╚════██║   ██║   ██╔══╝  ██║╚██╗██║██╔═══╝ ██╔══██╗██║   ██║
██║ ╚████║███████╗   ██║   ███████╗██║███████║   ██║   ███████╗██║ ╚████║██║     ██║  ██║╚██████╔╝
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
{_cyan}[+]CREATOR: {_white}https://github.com/alexemployed                                            {_cyan}Version:{_white} {_version}
                                                                                                  """)

host = input(f"{_yellow}[!]{_white} Enter the host: ")


if __name__ == '__main__':
    try:
        if os_name == 'Linux':
            if check_root() != 0:
                sys.exit("Run as sudo!")
            asyncio.run(scan_ports(host))
        
        if os_name == 'Windows':
            if check_admin():
                asyncio.run(scan_ports(host))
            else: sys.exit("Run as Admin")

    except KeyboardInterrupt:
        print(f"Program {_red}end{_white} by user!")
        sys.exit(0)
