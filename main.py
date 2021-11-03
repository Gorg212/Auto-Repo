import json, pyautogui
from make import make
import os, time

os.system("clear")
os.system("figlet AUTO REPO")

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