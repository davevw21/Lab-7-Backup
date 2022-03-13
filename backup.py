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
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

name = input("Please type your username: ")

identification = getpass.getpass(prompt="Please enter your password: ")

directory = Path.cwd()
backfile = 'csrBackup.txt'
q = datetime.datetime.now
write = "w"
f = open(backfile, write)
addy = '192.168.157.11'
vrouter = {'ip': addy, 'username': name, 'password': identification, 'device_type': 'cisco_ios'}

try:
    connection = ConnectHandler(**vrouter)
    output = connection.send_command('show run')
    f.write(output)
    f.close()
except (AuthenticationException):
    print("An authentication error has occored while connecting to: " + vrouter['ip'])
except (SSHException):
    print("An error has occured while connecting to device " + vrouter['ip'] + " via ssh.  Ensure SSH is enabled.")
except (NetMikoTimeoutException):
    print("The device " + vrouter['ip'] + "has timed out while attempting to connect")
