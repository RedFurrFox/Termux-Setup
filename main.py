# Needed python modules
import os
import random
import requests


# Dictionaries
Logo = """
,--------.                                                     ,---.             ,--.                    
'--.  .--'  ,---.  ,--.--. ,--,--,--. ,--.,--. ,--.  ,--.     '   .-'   ,---.  ,-'  '-. ,--.,--.  ,---.  
   |  |    | .-. : |  .--' |        | |  ||  |  \  `'  /      `.  `-.  | .-. : '-.  .-' |  ||  | | .-. | 
   |  |    \   --. |  |    |  |  |  | '  ''  '  /  /.  \      .-'    | \   --.   |  |   '  ''  ' | '-' ' 
   `--'     `----' `--'    `--`--`--'  `----'  '--'  '--'     `-----'   `----'   `--'    `----'  |  |-'  
                                                                                                 `--'    """
Credits = 'Created and being maintained by the "Blixors Group"'
Advertisement = 'Join our FB group "https://www.facebook.com/groups/1778790372291663"'
Version = "v1.0"  # Do not change!!! Unless you know what you are doing
Pingable_Url = "https://google.com"
Proxy_List = [
    "95.80.98.41:8080",
    "95.141.36.112:8686",
    "94.140.208.226:8080",
    "91.240.97.69:1080",
    "91.240.97.69:8080",
    "94.247.244.106:3128",
    "89.248.244.182:8080",
    "88.247.10.31:8080",
    "79.104.25.218:8080",
    "78.11.85.10:8080",
    "77.237.121.22:8080",
    "77.120.137.143:8080",
    "78.81.245.153:8080",
    "77.38.21.239:8080",
    "62.213.14.166:8080",
    "65.182.5.212:8080",
    "61.19.27.201:8080",
    "61.19.145.66:8080",
    "62.201.217.194:8080",
    "50.246.120.125:8080",
    "50.201.51.216:8080"
]
Useragent_List = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
    "Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
]
Header_Data = {
    "user-agent" : f'{random.choice(Useragent_List)}'
    
}


# Terminal Cleaner/Purger
def Clear_Terminal():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


# Main operation
def Main():

    # Checks if the user is online or not
    def Check_If_Online():
        # Prompting
        print("Checking for your internet connection status...")
        # Getting a requests
        if requests.get(
                        url     = Pingable_Url,
                        proxies = random.choice(Proxy_List),
                        headers = Header_Data
                        ) == 200 :
            print()


# Runner
if __name__ == "__main__":
    Clear_Terminal()
    Main()
