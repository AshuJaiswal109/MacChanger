#!/use/bin/env python
import subprocess
print("                             ")
print("\t########################################")
print("\t#       Welcome to Mac changer tool    #")
print("\t#       Created by @Ashujaiswal        #")
print("\t########################################")
print("                             ")
interface = raw_input("Enter your interface name ex: eth0, wlan0 : ")
print("                             ")
mac_address = raw_input("Enter new mac address: ")
print("                             ")
print("Voila! Mac address of interface " + interface + " changed successfully. New mac address is " + mac_address)
print("                             ")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)