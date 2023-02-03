# Jacob Hammargren
# picoCTF Automation
# level: get aHEAD

import requests

def run():
    url = 'http://mercury.picoctf.net:34561/index.php'
    flag = requests.head(url).headers['flag']
    return flag

