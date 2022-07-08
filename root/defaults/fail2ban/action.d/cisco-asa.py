#!/usr/bin/python
# emacs: -*- mode: python; indent-tabs-mode: t -*-
#
#
import sys
from netmiko import ConnectHandler

platform = 'cisco_asa'
host ='172.27.1.1'
username = 'fail2ban'
password = 'password'
enable_pass = 'enablepass'

acl_name = 'Fail2Ban'

def main(argv):
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password, secret=enable_pass)
    device.enable()
    device.config_mode()
    command = argv[1]
    ipaddr = argv[2]
    if command == 'ban':
        # Ban the IP
        print("Banning %s" % ipaddr)
        device.send_command('object-group network %s' % acl_name, expect_string='\(config-network-object-group\)\#')
        device.send_command('network-object host %s' % ipaddr, expect_string='\(config-network-object-group\)\#')
        device.send_command('clear conn address %s' % ipaddr, expect_string='\(config-network-object-group\)\#')
        device.send_command('exit', expect_string='\(config\)\#')
    elif command == 'unban':
        # UnBan the IP
        print("Un-Banning %s" % ipaddr)
        device.send_command('object-group network %s' % acl_name, expect_string='\(config-network-object-group\)\#')
        device.send_command('no network-object host %s' % ipaddr, expect_string='\(config-network-object-group\)\#')
        device.send_command('exit', expect_string='\(config\)\#')
    else:
        # Unknown command
        print("Unknown command")
    
    # All done, exit config mode
    device.send_command('exit', expect_string='\#')
    #device.send_command('copy running-config startup-config')           # save
    device.disconnect()


# Main
if __name__ == "__main__":
   main(sys.argv)
