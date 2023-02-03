# Jacob Hammargren
# picoCTF Automation
# level: Some Assembly Required

import requests
import re

def run():
    url = 'http://mercury.picoctf.net:36152/JIFxzHyW8W'
    data = requests.get(url).text
    flag = re.findall('(?=picoCTF).*}', data)
    return flag[0]

