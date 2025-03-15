# selectmenu.py
from dotenv import load_dotenv
import os
import subprocess
from time import sleep as wait
import sys
from packages.package import *

app_version = "1.0.0"
docurl = "https://github.com/triisdang/CreateSync/wiki"
load_dotenv()
github_name = os.getenv('GITHUBUSER')
github_repo = os.getenv('GITHUBNAMEREPO')

def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        open(file_path, "w").close()

try:
    with open("./CONFIG/info.txt") as f:
        ink = f.read().strip()
except FileNotFoundError:
    ink = "false"

os.system("clear" if os.name != "nt" else "cls")

def info(f):
    logo()
    print(f"Welcome, {github_name}")
    print("Welcome to CreateSync. To get started, go to:")
    print(docurl, "\n")
    print(f"VERSION {app_version}")
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
        print("[5] Apply")
        print("[6] Help")
        print("[7] RESET TO DEFAULT (DON'T DO THIS IF YOU DON'T KNOW WHAT YOU ARE DOING)")
        print("[X] Exit")
    userinput = input("Select an option: ").strip().upper()
    if userinput in ["1", "2", "3", "4", "5", "6", "7", "X"]:
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
            print("Syncing from cloud...")
            git_pull(github_repo, f'./CONFIG/{github_repo}')
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
        print("LINK DIR/FILE")
        file = input("Copy the directory and paste it here: ")
        file_path = f"./CONFIG/{github_repo}/scripts/linked.txt"
        ensure_file_exists(file_path)
        with open(file_path, "r+") as txt_file:
            content = txt_file.read().strip()
            txt_file.write(merge_lists(content, file))
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "5":
        print(f"Goto {docurl} for help!")
        wait(3)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "6":
        print(f"(Feature in progress)")
        wait(4)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "7" and f == "true":
        print("Are you sure you want to reset? It may break the code. [Y/N]")
        userinput = input().strip().upper()
        if userinput == "Y":
            with open("./CONFIG/info.txt", "w") as f:
                f.write("false")
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)

optioncheck(info(ink), ink)
