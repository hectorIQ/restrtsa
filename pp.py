import os, random, subprocess, signal, uuid, string
import re
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    xrblue = f"\n{blueplus} Instagram Password Reset {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@C_FG {BLUE}/ {WHITE}@C_FG"
class Xnce():
    def __init__(self):
        print(DESIGN.xrblue)
        print(f"\n{DESIGN.blueplus} Target: ", end="")
        self.target = input()
        if self.target[0]=="@":
            print(f"\n{DESIGN.redminus} Enter User Without {DESIGN.RED}@")
            self.inex()
        if "@" in self.target:
            usem = "user_email"
        else:
            usem = "username"
        self.data = {
            "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
            usem: self.target,
            "guid": uuid.uuid4(),
            "device_id": uuid.uuid4()
        }
        self.send_password_reset()
    def inex(self):
        
            
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
            
        input()
        os.kill(os.getpid(), signal.SIGTERM)
    def send_password_reset(self):
        head = {"user-agent": f"Instagram 195.0.0.31.123 Android (22/5.1; 160dpi; 768x976; unknown/generic; Google Nexus 6; vbox86p; goldfish; en_US; 302733773)"}
        req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=self.data)
        #print(req.text, req.status_code)
        if "obfuscated_email" in req.text: 
            print(f"{req.text}")
            print(f"\n{DESIGN.blueplus} {req.text}")
            Xnce()
        elif req.status_code==404:
            print(f'\n{DESIGN.redminus} "message":"No users found","status":"fail"')
            Xnce()
        else:
            print(f"\n{DESIGN.redminus} {req.text}")
            Xnce()
       
Xnce()
        