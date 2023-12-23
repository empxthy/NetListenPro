#! /usr/bin/python3

# Coding: UTF-8
# Name: TCP-Listener
# Author: AlexEmployed
# Version: 0.0.1
# License: GPL-3.0 version
# Copyright: alexemployed 2023
# Github: https://github.com/alexemployed
# Language: Python


# Imports
import sys
import os
import asyncio
import platform
import subprocess

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
