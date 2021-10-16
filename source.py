# import Modules > requests , uuid , os <
import requests , uuid , os
#import color from colorama
try:
    from colorama import Fore
except ModuleNotFoundError as Module:
    Module_PiP = str(Module).split("'")[1]
    os.system(f'pip install {Module_PiP}')
# Make uuid
Fid = uuid.uuid4()
# Make a variable for #user & Pass
username_req = input(f'{Fore.RED}>{Fore.RESET} Username : {Fore.RED}')
password_req = input(f'{Fore.RESET}{Fore.RED}>{Fore.RESET} Password : {Fore.RED}')
def REQ():
    # make a requests
    Headers_req = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    'Accept': "*/*",
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-Connection-Type': 'WIFI',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com'
    }
    Data_req = {
    'uuid': Fid,
    'password': password_req,
    'username': username_req,
    'device_id': Fid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
    'login_attempt_countn': '0'
    }
    Url_req = "https://i.instagram.com/api/v1/accounts/login/"
    Login_req = requests.request("POST",Url_req,headers=Headers_req,data=Data_req)
    # Get response
    if ("is_private") in Login_req.text:
        cookies = Login_req.cookies
        print(f'{Fore.RESET}{Fore.RED}>{Fore.RESET} Login True : @{username_req}{Fore.RED}')
        # Make a variable for New Name
        New_Name_req = input(f'{Fore.RED}>{Fore.RESET} New Name : {Fore.RED}')
        # Make a requests for change name
        change_name_data = {'first_name': New_Name_req}
        Change_name_req = requests.request("POST",('https://i.instagram.com/api/v1/accounts/set_phone_and_name/'),headers=Headers_req,data=change_name_data,cookies=cookies)
        if ('"status":"ok"') in Change_name_req.text:
            print(f'{Fore.RESET}{Fore.RED}>{Fore.RESET} Done Set Name {Fore.RED}')
            input('>')
        elif ('"Ensure this value has at most 30 characters') in Change_name_req:
            print(f'{Fore.RESET}{Fore.RED}>{Fore.RESET} Name Is To Long ! {Fore.RED}')
            REQ()
        else:
            print(f'{Fore.RESET}{Fore.RED}>{Fore.RESET} Error !!!!{Fore.RED}')
            print(Change_name_req.text)
    else:
        print(f'{Fore.RESET}{Fore.RED}>{Fore.RESET} Login False : @{username_req}{Fore.RED}')
        print(f"{Fore.RESET}{Fore.RED}>{Fore.RESET} {Login_req.text}")



REQ()
