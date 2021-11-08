import json, pyautogui
from make import make
import os, time

os.system("clear")
print('             _                               ')
print('  __ _ _   _| |_ ___    _ __ ___ _ __   ___  ')
print(' / _` | | | | __/ _ \  | '__/ _ \ '_ \ / _ \ ')
print('| (_| | |_| | || (_) | | | |  __/ |_) | (_) |')
print(' \__,_|\__,_|\__\___/  |_|  \___| .__/ \___/ ')
print('                                |_|          ')

try:
    open('data.json')
except:
    make()

rname = input("repo name: ")


with open('data.json', 'r') as f:
    load  = json.loads(f.read())

user = load['usr']
token = load['pass']
repo = f'"name":"{rname}"'
# print(repo)
print('curl -u "' + user + ':'+ token +'" https://api.github.com/user/repo -d \'{' +repo+ '}\'')
os.system('curl -u "' + user + ':'+ token +'" https://api.github.com/user/repos -d \'{' +repo+ '}\'')

clonePath = input("Please enter the path to where you want to clone the repo: ")

# os.system(f'cd {clonePath}')
os.system(f'git clone https://github.com/{user}/{rname} {clonePath}/{rname}')
