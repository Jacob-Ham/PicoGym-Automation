#!/bin/bash
# Jacob Hammargren
# picoCTF Automation
# level: Cookies
import requests
import re

def run():
    flag = []
    dir = ['', 'mycss.css', 'robots.txt', '.htaccess', '.DS_Store']
    regex = ['(?=picoCTF).*t', '(?<=part 2: ).*l0', '(?<=Part 3: ).*4c', '(?<=Part 4: ).*0k', '(?<=Part 5: ).*}']
    url = 'http://mercury.picoctf.net:39698/'
    
    for i in range(len(dir)):
        data = requests.post(url + dir[i]).text
        flag.append(re.findall(regex[i], data))
    flag = flag[0][0] + flag[1][0] + flag[2][0] + flag[3][0] + flag[4][0]

    return flag