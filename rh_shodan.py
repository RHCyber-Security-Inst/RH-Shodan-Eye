#!/usr/bin/env/python3
# This Python file uses the following encoding:utf-8

# Author: Jolanda de Koff
# GitHub: https://github.com/
# Website: https://rhcybersecurity.com


# Your Shodan API Key can be found here: https://account.shodan.io

########################################################################

# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################


import os
import random
import shodan
import time
import sys

# RH|Shodan v1.4.0

banner1 = ("""

\033[1;31m

  _____  _    _ _  _____ _    _  ____  _____          _   _ 
 |  __ \| |  | | |/ ____| |  | |/ __ \|  __ \   /\   | \ | |
 | |__) | |__| | | (___ | |__| | |  | | |  | | /  \  |  \| |
 |  _  /|  __  | |\___ \|  __  | |  | | |  | |/ /\ \ | . ` |
 | | \ \| |  | | |____) | |  | | |__| | |__| / ____ \| |\  |
 |_|  \_\_|  |_| |_____/|_|  |_|\____/|_____/_/    \_\_| \_|
               | |                                          
               |_|                                          

\033[1;m
            \033[1;31mRH|Shodan v1.4.0\033[0m

    ✓ The author is not responsible for any damage, misuse of the information.
    ✓ RH|Shodan shall only be used to expand knowledge and not for
      causing malicious or damaging attacks.
    ✓ Just remember, Performing any hacks without written permission is illegal ..!

            Author    :  Jolanda de Koff Bulls Eye
            Developed :  RH|Cyber-Security & Ethical Hacking Inst.
            Website   :  https://rhcybersecurity.com


            \033[1;31mHi there, Shall we play a game..?\033[0m 😃
        """)

banner2 = ("""

\033[1;31m

                                                                                          
                                                                                          
________   ____    ____MM   ____  ____    ____   ____   ________        _     ___      ___
`MMMMMMMb. `MM'    `MM'MM  6MMMMb\`MM'    `MM'  6MMMMb  `MMMMMMMb.     dM.    `MM\     `M'
 MM    `Mb  MM      MM MM 6M'    ` MM      MM  8P    Y8  MM    `Mb    ,MMb     MMM\     M 
 MM     MM  MM      MM MM MM       MM      MM 6M      Mb MM     MM    d'YM.    M\MM\    M 
 MM     MM  MM      MM MM YM.      MM      MM MM      MM MM     MM   ,P `Mb    M \MM\   M 
 MM    .M9  MMMMMMMMMM MM  YMMMMb  MMMMMMMMMM MM      MM MM     MM   d'  YM.   M  \MM\  M 
 MMMMMMM9'  MM      MM MM      `Mb MM      MM MM      MM MM     MM  ,P   `Mb   M   \MM\ M 
 MM  \M\    MM      MM MM       MM MM      MM MM      MM MM     MM  d'    YM.  M    \MM\M 
 MM   \M\   MM      MM MM       MM MM      MM YM      M9 MM     MM ,MMMMMMMMb  M     \MMM 
 MM    \M\  MM      MM MM L    ,M9 MM      MM  8b    d8  MM    .M9 d'      YM. M      \MM 
_MM_    \M\_MM_    _MM_MM MYMMMM9 _MM_    _MM_  YMMMM9  _MMMMMMM9_dM_     _dMM_M_      \M 
                       MM                                                                 
                       MM                                                                 
                       MM

\033[1;m
        \033[1;31mRH|Shodan v1.4.0\033[0m

    ✓ The author is not responsible for any damage, misuse of the information.
    ✓ RH|Shodan shall only be used to expand knowledge and not for
      causing malicious or damaging attacks.
    ✓ Just remember, Performing any hacks without written permission is illegal ..!

            Author   :  Jolanda de Koff Bulls Eye
            Developed:  RH|Cyber-Security & Ethical Hacking Inst.
            Website  :  https://rhcybersecurity.com

            \033[1;31mHi there, Shall we play a game..?\033[0m 😃
        """)

choi = (banner1, banner2)
print (random.choice(choi))
time.sleep(0.5)

data = input("\n[+] \033[34mDo you like to save the output in a file? \033[0m(Y/N) ").strip()
l0g = ("")


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(data)
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("\n[~] \033[34mGive the file a name: \033[0m ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] \033[34mSaving is skipped\033[0m")
    print ("\n" + "  " + "»" * 78 + "\n")


def showdam():
    if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
        with open("api.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("api.txt", "w")
        os.system("stty -echo")
        shodan_api_key = input("[!] \033[34mEenter a valid Shodan API Key: \033[0m")
        os.system("stty echo")
        file.write(shodan_api_key)
        print ("\n[~] \033[34mFile written: ./api.txt \033[0m")
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.4)

    limit = 888  # Just a number
    counter = 1

    try:
        print ("[~] \033[34mChecking Shodan.io API Key... \033[0m")
        api.search("b00m")
        print ("[✓] \033[34mAPI Key Authentication:\033[0m SUCCESS..!")
        time.sleep(0.5)
        b00m = input("\n[+] \033[34mEnter your keyword(s):\033[0m ")
        counter = counter + 1
        for banner in api.search_cursor(b00m):
            print ("[+] \033[1;31mIP: \033[1;m" + (banner["ip_str"]))
            print ("[+] \033[1;31mPort: \033[1;m" + str(banner["port"]))
            print ("[+] \033[1;31mOrganization: \033[1;m" + str(banner["org"]))
            print ("[+] \033[1;31mLocation: \033[1;m" + str(banner["location"]))
            print ("[+] \033[1;31mLayer: \033[1;m" + (banner["transport"]))
            print ("[+] \033[1;31mLayer: \033[1;m" + (banner["transport"]))
            print ("[+] \033[1;31mDomains: \033[1;m" + str(banner["domains"]))
            print ("[+] \033[1;31mHostnames: \033[1;m" + str(banner["hostnames"]))
            print ("[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (banner["data"]))
            print ("\n[✓] Result: %s. Search query: %s" % (str(counter), str(b00m)))

            data = ("\nIP: " + banner["ip_str"]) + ("\nPort: " + str(banner["port"])) + ("\nOrganisation: " + str(banner["org"])) + ("\nLocation: " + str(banner["location"])) + ("\nLayer: " + banner["transport"]) + ("\nDomains: " + str(banner["domains"])) + ("\nHostnames: " + str(banner["hostnames"])) + ("\nData\n" + banner["data"])
            logger(data)
            time.sleep(0.1)
            print ("\n" + "  " + "»" * 78 + "\n")

            counter += 1
            if counter >= limit:
                exit()

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    except shodan.APIError as oeps:
            print ("[✘] \033[1;31mError: %s \033[0m" % (oeps))
            sha_api = input("[*] \033[34mWould you like to change the API Key? <Y/N>:\033[0m ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api.txt", "w")
                os.system("stty -echo")
                shodan_api_key = input("[✓] \033[34mPlease enter valid Shodan.io API Key:\033[0m ")
                os.system("stty echo")
                file.write(shodan_api_key)
                print ("\n[~] \033[34mFile written: ./api.txt\033[0m")
                file.close()
                print ("[~] \033[34mRestarting the Platform, Please wait...\033[0m \n")
                time.sleep(1)
                showdam()
            else:
                print ("")
                print ("[•] Exiting Platform... \033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
                sys.exit()

    print ("\n\n\tShodan Eye \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")


# =====# Main #===== #
if __name__ == "__main__":
    showdam()

