import argparse
import json
import random
from googleapiclient.discovery import build
from dotenv import load_dotenv, dotenv_values

# config
load_dotenv()
config = dotenv_values(".env")

channelIds = ["UC8butISFwT-Wl7EV0hUK0BQ", "UC-yuWVUplUJZvieEligKBkA", "UC29ju8bIPH5as8OGnQzwJyA", "UCsBjURrPoezykLs9EqgamOA", "UCJZv4d5rbIKd4QHMPkcABCw", "UCW5YeuERMmlnqo4oq8vwUpg", "UC9-y-6csu5WGm29I7JiwpnA", "UCYO_jab_esuFRV4b17AJtAw", "UCYbK_tjZ2OrIZFBvU6CCMiA", "UCmtyQOKKmrMVaKuRXz02jbQ", "UClcE-kVhqyiHCcjYwcpfj9w", "UCVeW9qkBjo3zosnqUbG7CFw", "UCOKHwx1VCdgnxwbjyb9Iu1g", "UC4JX40jDee_tINbkjycV4Sg", "UCwRXb5dUK4cvsHbx-rGzSgw", "UCS0N5baNlQWJCUrhCEo8WlA", "UCZUyPT9DkJWmS_DzdOi7RIA"]

client = build("youtube", "v3", developerKey=config["API_KEY"])

def search(channelId):
    search_response = client.search().list(
        part="snippet",
        channelId=channelId,
        type="video",
        order="date",
        maxResults=25
    ).execute()

    projects = []

    for i in range(len(search_response["items"])):
        projects.append({
            "title": search_response["items"][i]["snippet"]["title"],
            "link": f"https://www.youtube.com/watch?v={search_response['items'][i]['id']['videoId']}&t=1s&ab_channel={search_response['items'][i]['snippet']['channelTitle']}"
        })

    return projects

if __name__ == '__main__':
    returnList = [];

    for i in range(len(channelIds)):
        for val in search(channelIds[i]):
            returnList.append(val)

    returnListLength = len(returnList)

    print("Welcome to Project Picker.")
    print(f"I have got {returnListLength} project{'s' if returnListLength > 1 else ''} for you.")

    while True:
        userChoice = input("Press 'any key' to continue  or 'q' to quit: ")
        
        if userChoice == "q":
            break;

        print("")

        randomNum = random.randint(0, len(returnList))
    
        print(returnList[randomNum]["title"])
        print(returnList[randomNum]["link"])
        print("")


        

