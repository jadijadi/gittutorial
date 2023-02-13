import socket
import time
import os

"""
This functions checks connection to Google DNS server
If DNS server is reachable on port 53, then it means that
the internet is up and running
"""

#Initial Marks for Connectivity or not
check = "\N{Heavy Check Mark}"
fail = "\N{Heavy Multiplication X}"

def internet_connected(host="8.8.8.8", port=53):
    """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
    try:
        socket.setdefaulttimeout(1)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        pass

    return False


try:
    # Store value of last state in this variable
    counter = 0
    while True:
        if internet_connected():
            # find out what is the os
            uname = os.uname()
            # Clear Command line Session
            if uname.sysname == 'Linux' or uname.sysname == 'Darwin':
                os.system('clear')
                print(f"You are on a {uname.sysname} machine")
            elif uname.sysname == 'Windows':
                os.system('cls')
                print("You are on a Windows  machine")

            counter += 1
            print(f"Internet is up {check}\n{counter} sec \n{round(counter / 60, 2)} min \n{round(counter / 3600, 2)} hour\n")

            # Wait for 1 second before checking for internet connectivity
            time.sleep(1)
        else:
            # If previously internet connected, then print message
            print(f"Internet is down ... {fail}")

except KeyboardInterrupt:
    print("Exiting... Bye!")
