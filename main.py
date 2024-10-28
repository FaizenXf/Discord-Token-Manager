'''
                    GNU GENERAL PUBLIC either of
<https://www.gnu.org/licenses/why-not-lgpl.html>.
'''
'''
~ https://discord.gg/lgnop
~ KaramveerPlayZ#1337
'''
import httpx
from tasksio import TaskPool
import asyncio
import sys
from typing import Optional
import os
import aiohttp
import secrets
import base64
import time
from colorama import Fore, init

def clear():
  if sys.platform in ["linux", "linux2"] or os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")



def setTitle(title: Optional):
  os.system("title "+title)

clear()
setTitle("KaramveerPlayZ#1337 - Token Manager")

base_url = "https://discord.com/api/v9/users/@me"
tokens = []

def Check_Tokens():
  for tk in open('tokens.txt', 'r').readlines():
    t = tk.strip()
    r = httpx.get(base_url, headers={"Authorization": t})
    if r.status_code in [204, 200, 201]:
      print(f"[-] Token Vaild - {t[:20]}***************")
      tokens.append(t)

Check_Tokens()
time.sleep(2)

if tokens == []:
  print("[-] All Tokens Were Invaild, Retry Later With Vaild Tokens.")
  sys.exit()

                 

  
def getheaders(Toke):
  header = {
			'Authorization': Toke,
			'accept': '*/*',
			'accept-language': 'en-US',
			'connection': 'keep-alive',
			'cookie': f'__cfduid = {secrets.token_hex(43)}; __dcfduid={secrets.token_hex(32)}; locale=en-US',
			'DNT': '1',
			'origin': 'https://discord.com',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'referer': 'https://discord.com/channels/@me',
			'TE': 'Trailers',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
			'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
		}
  return header

async def change_bio(token, bio):
  headers = getheaders(token)
  async with aiohttp.ClientSession(headers=headers) as httpClient:
    async with httpClient.patch(base_url, json={"bio": bio}) as response:
      if response.status in (204, 200, 201, 500, 299):
        print(f"[-] Changed Bio, Token: {token[:20]}***************")
      else:
        print(f"[-] Unable To Change Bio, Token: {token[:20]}***************")

  
async def change_username(token, name, dexterkimakalunduskebaapkichutme):
  headers = getheaders(token)
  async with aiohttp.ClientSession(headers=headers) as httpClient:
    async with httpClient.patch(base_url, json={"username": name, "password": dexterkimakalunduskebaapkichutme}) as response:
      if response.status in (204, 200, 201, 500, 299):
        print(f"[-] Changed Name, Token: {token[:20]}***************")
      else:
        print(f"[-] Unable To Change Name, Token: {token[:20]}***************")

async def change_avatar(luli):
  headers = getheaders(luli)
  img = open('image.png', 'rb').read()
  async with aiohttp.ClientSession(headers=headers) as httpClient:
    async with httpClient.patch(base_url, json={"avatar":f'data:image/png;base64,{base64.b64encode(img).decode("ascii")}'}) as loda:
      if loda.status in (204, 200, 201, 299, 500):
        print(f"[-] Changed Avatar, Token: {luli[:20]}***************")
      else:
        print(f"[-] Unable To Change Avatar, Token: {luli[:20]}***************")

async def change_password(token, lund, condom):
  headers = getheaders(token)
  async with aiohttp.ClientSession(headers=headers) as httpClient:
    async with httpClient.patch(base_url, json={"password": lund, "new_password": condom}) as nvmm:
      if nvmm.status in (204, 200, 201, 299, 500):
        tk = await nvmm.json()
        with open('new_tokens.txt', 'w') as f:
          tkn = tk['token']
          f.write(tkn+"\n")
          print(f"[-] Changed Password And Saved New Token in new_tokens.txt, Token: {token[:20]}***************")
      else:
          print(f"[-] Unable To Change Password, Token: {token[:20]}***************")

async def pc():
  password = input(f"[-] Enter Tokens Password: ")
  new_password = input(f"[-] Enter New Password: ")
  async with TaskPool(10_000) as pool:
    for token in tokens:
      await pool.put(change_password(token, password, new_password))

async def uc():
  username = input("[-] Enter New Username: ")
  password = input("[-] Enter Tokens Password: ")
  async with TaskPool(10_000) as pool:
    for token in tokens:
      await pool.put(change_username(token, username, password))

async def bo():
  b = input("[-] Enter New Bio: ")
  async with TaskPool(10_000) as pool:
    for token in tokens:
      await pool.put(change_bio(token, b))

async def ac():
  async with TaskPool(10_000) as pool:
    for token in tokens:
      await pool.put(change_avatar(token))

menu = f"""[{Fore.RED}-{Fore.RESET}] Created By KaramveerPlayZ#1337, https://discord.gg/lgnop\n\n[{Fore.RED}1{Fore.RESET}] - Username Changer\n[{Fore.RED}2{Fore.RESET}] - Password Changer\n[{Fore.RED}3{Fore.RESET}] - Avatar Changer\n[{Fore.RED}4{Fore.RESET}] - Bio Changer\n"""
clear()
print(menu)

option = input(f"[-] Choice: ")

try:
  o = int(option)
except ValueError:
  print("[-] Option Must Be Integer.")
  sys.exit()

if o == 1:
  asyncio.run(uc())
elif o == 2:
  asyncio.run(pc())
elif o == 3:
  asyncio.run(ac())
elif o == 4:
  asyncio.run(bo())

if __name__ == "__main__":
  init()
