# !/usr/bin/env python3

import subprocess
import re

def mac_change(interface,new_mac):
    try:
        subprocess.call(['ifconfig',interface,'down'])
        subprocess.call(['ifconfig',interface,'hw','ether',new_mac])
        subprocess.call(['ifconfig',interface,'up'])
    
    except :
        print("something ERROR is occurs")

def verify(interface,new_mac):
    ifconfig_data = str(subprocess.check_output(["ifconfig",interface]))           
    ether = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_data)
    print(ether.group(0))

    if (ether.group(0) == new_mac) :
        print(f"[+] Mac is Changed to {ether.group(0)}")
    else :
        print("some ERROR occurs")


interface = input("enter here interface: ")
new_mac = input("enter new mac: ") 

mac_change(interface,new_mac)
verify(interface,new_mac)
