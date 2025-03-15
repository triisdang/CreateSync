from dotenv import load_dotenv
import os
import subprocess
from time import sleep as wait
import sys

app_version = "1.0.0"
docurl = "[WIP]"
load_dotenv()
github_name = os.getenv('GITHUBUSER')

# Read config file
try:
    with open("./CONFIG/info.txt") as f:
        ink = f.read().strip()
except FileNotFoundError:
    ink = "false"  # Default if file is missing

os.system("clear" if os.name != "nt" else "cls")

def logo() :
    print("┏┓         ┏┓     ")
    print("┃ ┏┓┏┓┏┓╋┏┓┗┓┓┏┏┓┏")
    print("┗┛┛ ┗ ┗┻┗┗ ┗┛┗┫┛┗┗")
    print("              ┛   ")
    print("-----------------------------")



def info(f):
    logo()
    print(f"Welcome, {github_name}")
    print("Welcome to CreateSync. To get started, go to:")
    print(docurl, "\n")

    if f == "false":
        print("[1] Clone repo")
        print("[2] Sync from cloud")
        print("[3] Sync to cloud")
        print("[4] Edit config (COMING SOON)")
        print("[5] Help")
        print("[X] Exit")
    else:
        print("[1] Sync from cloud")
        print("[2] Sync to cloud")
        print("[3] Edit config (COMING SOON)")
        print("[4] Add files, dir")
        print("[5] Help")
        print("[6] RESET TO DEFAULT (DON'T DO THIS IF YOU DON'T KNOW WHAT YOU ARE DOING)")
        print("[X] Exit")

    userinput = input("Select an option: ").strip().upper()
    
    if userinput in ["1", "2", "3", "4", "5", "X"]:
        return userinput
    else:
        print("Unknown option, try again!")
        wait(3)
        os.system("clear" if os.name != "nt" else "cls")
        return info(f)

def optioncheck(option, f):
    if option == "1":
        if f == "false":
            subprocess.run(["python3", "clone.py"])
        else:
            print("Syncing from cloud... (Feature in progress)")
            wait(2)
            os.system("clear" if os.name != "nt" else "cls")
            optioncheck(info(f), f)

    elif option == "2":
        print("Syncing to cloud... (Feature in progress)")
        wait(2)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)

    elif option == "3":
        print("Editing config... (Feature in progress)")
        wait(2)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)

    elif option == "4":
        print(f"(Feature in progress)")
        wait(2)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)

    elif option == "5":
        print(f"Goto {docurl} for help!")
        wait(3)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)

    elif option == "6" and f == "true":
        print("Are you sure you want to reset? It may break the code. [Y/N]")
        userinput = input().strip().upper()
        if userinput == "Y":
            with open("./CONFIG/info.txt", "w") as f:
                f.write("false")
        else:
            os.system("clear" if os.name != "nt" else "cls")
            optioncheck(info(f), f)



optioncheck(info(ink), ink)
