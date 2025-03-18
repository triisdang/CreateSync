from dotenv import load_dotenv
import os
import subprocess
from time import sleep as wait
import sys
import json
import shutil
from packages.package import *

app_version = "1.0.0"
docurl = "https://github.com/triisdang/CreateSync/wiki"
load_dotenv()
github_name = os.getenv('GITHUBUSER')
github_repo = os.getenv('GITHUBNAMEREPO')
config = "../config"
def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        open(file_path, "w").close()

try:
    with open("{config}/info.txt") as f:
        ink = f.read().strip()
except FileNotFoundError:
    ink = "false"

os.system("clear" if os.name != "nt" else "cls")

def sync_from_cloud():
    shared_folder = f"{config}{github_repo}/shared"
    os.makedirs(shared_folder, exist_ok=True)
    linked_path = f"{config}/{github_repo}/scripts/linked.txt"
    try:
        with open(linked_path, "r") as f:
            linked_list = json.load(f)
    except Exception:
        linked_list = []
    for item in linked_list:
        dest_path = os.path.join(f"{config}/{github_repo}", item)
        src_path = os.path.join(shared_folder, os.path.basename(item))
        if not os.path.exists(dest_path):
            if os.path.exists(src_path):
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dest_path)
                elif os.path.isfile(src_path):
                    shutil.copy2(src_path, dest_path)
                print(f"Synced {item} from shared folder.")
            else:
                print(f"No shared copy found for {item}.")
        else:
            print(f"{item} already exists in repo.")

def apply_linked():
    shared_folder = f"{config}/{github_repo}/shared"
    os.makedirs(shared_folder, exist_ok=True)
    linked_path = f"{config}/{github_repo}/scripts/linked.txt"
    try:
        with open(linked_path, "r") as f:
            linked_list = json.load(f)
    except Exception:
        linked_list = []
    for item in linked_list:
        src_path = os.path.join(f"{config}/{github_repo}", item)
        dest_path = os.path.join(shared_folder, os.path.basename(item))
        if not os.path.exists(src_path):
            print(f"Source {item} does not exist in repo.")
        else:
            if os.path.exists(dest_path):
                if os.path.isdir(dest_path):
                    shutil.rmtree(dest_path)
                else:
                    os.remove(dest_path)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
            elif os.path.isfile(src_path):
                shutil.copy2(src_path, dest_path)
            print(f"Applied {item} to shared folder.")

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
            git_pull(github_repo, f'{config}/{github_repo}')
            sync_from_cloud()
            wait(2)
            os.system("clear" if os.name != "nt" else "cls")
            optioncheck(info(f), f)
    elif option == "2":
        print("Syncing to cloud...")
        wait(2)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "3":
        print("Editing config... (Feature working in progress)")
        wait(2)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "4":
        print("LINK DIR/FILE")
        file_input = input("Copy the directory and paste it here: ")
        file_path = f"{config}/{github_repo}/scripts/linked.txt"
        ensure_file_exists(file_path)
        with open(file_path, "r+") as txt_file:
            content = txt_file.read().strip()
            new_content = merge_lists(content, file_input)
            txt_file.seek(0)
            txt_file.truncate()
            txt_file.write(new_content)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "5":
        print("Applying linked directories to shared folder...")
        apply_linked()
        wait(3)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "6":
        print(f"Goto {docurl} for help!")
        wait(3)
        os.system("clear" if os.name != "nt" else "cls")
        optioncheck(info(f), f)
    elif option == "7" and f == "true":
        print("Are you sure you want to reset? It may break the code. [Y/N]")
        userinput = input().strip().upper()
        if userinput == "Y":
            with open("{config}/info.txt", "w") as f:
                f.write("false")
        os.system("clear" if os.name != "nt" else "cls")
        exit()

optioncheck(info(ink), ink)
