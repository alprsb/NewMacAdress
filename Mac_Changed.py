import subprocess
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="int_help")
    parse_object.add_option("-m", "--mac", dest="mac_adress", help="mac_help")
    return parse_object.parse_args()

def macChanged(user_interface,user_mac_adress ):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_adress])
    subprocess.call(["ifconfig", user_interface, "up"])
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig.decode("utf-8"))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac changed is sucessful")
(user_input,arguments) =get_user_input()
macChanged(user_input.interface,user_input.mac_adress)
final_mac = control_new_mac(user_input.interface)
print(final_mac)

if final_mac == user_input.mac_adress:
    print("You made it!!")
else:
    print("I'm sorry you fail :(")
