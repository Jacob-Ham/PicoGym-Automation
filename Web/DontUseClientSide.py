#!/bin/bash
# Jacob Hammargren
# picoCTF Automation
# level: Cookies

import requests
import re

def run():
    url = 'https://jupiter.challenges.picoctf.org/problem/29835/'
    data = requests.get(url).text
    flag = re.findall('(?<=[\'])\w+{*}*', data)
    flag = flag[0] + flag[2] + flag[6] + flag[4] + flag[3] + flag[5] + flag[1] + flag[7]
    return flag
