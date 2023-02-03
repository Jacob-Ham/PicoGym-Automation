#!/bin/bash
# Jacob Hammargren
# picoCTF Automation
# level: Cookies

import requests
import re

def run():
    flag = []
    dir = ['', 'mycss.css', 'myjs.js']
    regex = ['(?=picoCTF).*d3', '(?<=flag: ).*5t', '(?<=flag: ).*}']
    url = 'https://jupiter.challenges.picoctf.org/problem/44924/'

    for i in range(len(dir)):
        data = requests.post(url + dir[i]).text
        flag.append(re.findall(regex[i], data))
        
    flag = flag[0][0] + flag[1][0] + flag[2][0]
    
    return flag
