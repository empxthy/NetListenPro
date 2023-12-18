#! /usr/bin/python3

# Coding: UTF-8
# Name: TCP-Listener
# Author: AlexEmployed
# Version: 0.0.1
# License: MIT
# Copyright: alexemployed (2023-infinity)
# Github: https://github.com/alexemployed
# Language: Python


"""
MIT License

Copyright (c) 2023 Alex

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

# Imports
import sys
import asyncio

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
host = input(f"{_yellow}[!]{_white} Enter the host: ")


if __name__ == '__main__':
    try:
        asyncio.run(scan_ports(host))
    except KeyboardInterrupt:
        print(f"Program {_red}end{_white} by user!")
        sys.exit(0)