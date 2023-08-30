#########################################################
# DISCLAIMER                                            #
# PLEASE USE THIS TOOL FOR EDUCATIONAL PURPOSES ONLY.   #
#########################################################


# Import necessary modules
import subprocess
import datetime
import platform
import pyfiglet
import socket
import re


# Clear the terminal
if platform.system().lower() == 'windows':
    command = 'cls'
else:
    command = 'clear'
subprocess.call(command, shell=True)

# Print a neat banner
banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

# Scan type
print("For scanning using a domain, type <domain>.\nFor scanning using an IP address, type <ip>.")
print("Type <q> to abort the operation.")

# IP address pattern to validating
ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

while True:
    # All this terrifying while loop does is to check the given input at "scan_type".
    # If it is "q", then it will abort operation and quit program.
    # If it is "ip", then it will validate the IP address. If it is valid, then it will break the loop.
    # If it is "domain", then it will get the domain name and break the loop.
    # If it is none of the above, it will let the user know that the input is not valid.
    scan_type = input("\n>>> ")
    if scan_type.lower() == 'q':
        quit()
    if scan_type.lower() == 'ip':
        while True:
            host = input("\nEnter a IP to scan: ")
            if host.lower() == 'q':
                quit()
            if not re.match(ip_pattern, host):
                print("Invalid IP address.")
                continue
            else:
                break
        break
    elif scan_type.lower() == 'domain':
        host = input("\nEnter a domain to scan: ")
        if host.lower() == 'q':
            quit()
        else:
            break
    else:
        print("Invalid input.")
        continue

# Get the IP address of the domain name
hostIP = socket.gethostbyname(host)

# Get the range of the ports to scan
# Then split the starting and ending port
port_range = input("Enter port range in format <start>-<end> (ex: 20-80):\n>>> ")
port_range = port_range.split("-")

# Make a neat banner again
print("_"*60)
print("Scanning host: ", hostIP)
print(f"Scanning ports: {port_range[0]} to {port_range[1]}")
# Scan starting time
start_time = datetime.datetime.now()
print("Scan started at: ", start_time)
print("_"*60)

# Start scanning
print("\nPort\t\t\tStatus\n")
open_ports_counter = 0

for port in range(int(port_range[0]), int(port_range[1])+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Timeout for scanning each port is half a second
    s.settimeout(0.5)

    connection = s.connect_ex((hostIP, port))

    # Check whether a port is open or not
    # If it is open, print the port and its status
    # If it is not open, pass it
    if connection == 0:
        print(f"{port}\t----------\tOpen")
        open_ports_counter += 1
    else:
        pass

    s.close()

# Scan ending time
end_time = datetime.datetime.now()

# Make a neat banner again
print("_"*60)
print("Scan ended at: ", end_time)
print("Total open ports: ", open_ports_counter)
print("Time taken: ", end_time - start_time)
print("_"*60)

input("\nPress any key to continue...")