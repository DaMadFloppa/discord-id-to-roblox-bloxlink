# made by DaMadFloppa#9999

# importing
import os
import json
import requests

def clear():
	import os
	os.system('cls')

def maini():
	ID = input("Discord User ID: ")
	r = requests.get(f"https://api.blox.link/v1/user/{ID}")
	try:
		status = r.json().pop("status")
		main = r.json().pop("primaryAccount")
		print(f"\n{ID} Info\nMain Username: {main}\nStatus = {status} \n")
	except:
		print(f"Error, cannot fetch an account, this user may not have connected their ROBLOX account to their Discord. \n")

	username = r.json().pop("primaryAccount")
	f = requests.get(f"https://users.roblox.com/v1/users/{username}")
	try:
		user = f.json().pop("name")
		display = f.json().pop("displayName")
		banstatus = f.json().pop("isBanned")
		print(f"\nAdvanced User Info:\nUsername: {user}\nDisplay Name: {display}\nUser Banned?: {banstatus}\n")
	except:
		print("Error fetching advanced info.")

	end = input("Press enter to exit.")

maini()