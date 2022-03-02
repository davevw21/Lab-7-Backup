#Backup a network device
#Lab 7

import datetime
import pathlib
import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from pathlib import Path
import getpass
name = input("Please type your username: ")

identification = getpass.getpass(prompt="Please enter your password: ")

directory = Path.cwd()
backfile = 'csrBackup.txt'
q = datetime.datetime.now
write = "w"
f = open(backfile, write)
addy = '192.168.157.11'
vrouter = {'ip': addy, 'username': name, 'password': identification, 'device_type': 'cisco_ios'}
connection = ConnectHandler(**vrouter)
output = connection.send_command('show run')
f.write(output)
f.close() 
