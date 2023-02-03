# Jacob Hammargren
# picoCTF Automation
# level: Where Are The Robots

import requests
import re

def run():
    url = 'https://jupiter.challenges.picoctf.org/problem/60915/8028f.html'
    data = requests.get(url).text
    flag = re.findall('(?=picoCTF).*}', data)
    return flag[0]

