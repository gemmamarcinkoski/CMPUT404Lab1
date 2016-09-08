# encoding:utf-8

import requests

response = requests.get('https://github.com/gemmamarcinkoski/CMPUT404Lab1/raw/master/lab1/lab1script.py')

print response.text

