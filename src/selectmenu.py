from dotenv import load_dotenv
import os
import subprocess
from time import sleep as wait
import json
import shutil
from packages.package import *

app_version = "1.0.0"
docurl = "https://github.com/triisdang/CreateSync/wiki"
load_dotenv()
github_name = os.getenv('GITHUBUSER')
github_repo = os.getenv('GITHUBNAMEREPO')

config = os.path.abspath(os.path.join(os.getcwd(), "config"))

def ensure_file_exists(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    open(file_path, "a").close()

info_file = os.path.join(config, "info.txt")

try:
    with open(info_file) as f:
        ink = f.read().strip()
except FileNotFoundError:
    ink = "false"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

def sync_from_cloud():
    shared_folder = os.path.join(config, github_repo, "shared")
    os.makedirs(shared_folder, exist_ok=True)
    linked_path = os.path.join(config, github_repo, "scripts", "linked.txt")

    try:
        with open(linked_path, "r") as f:
            linked_list = json.load(f)
    except Exception:
        linked_list = []

    for item in linked_list:
        dest_path = os.path.join(config, github_repo, item)
        src_path = os.path.join(shared_folder, os.path.basename(item))
        if not os.path.exists(dest_path):
            if os.path.exists(src_path):
                shutil.copytree(src_path, dest_path) if os.path.isdir(src_path) else shutil.copy2(src_path, dest_path)
                print(f"Synced {item} from shared folder.")
            else:
                print(f"No shared copy found for {item}.")
        else:
            print(f"{item} already exists in repo.")

def apply_linked():
    shared_folder = os.path.join(config, github_repo, "shared")
    os.makedirs(shared_folder, exist_ok=True)
    linked_path = os.path.join(config, github_repo, "scripts", "linked.txt")

    try:
        with open(linked_path, "r") as f:
            linked_list = json.load(f)
    except Exception:
        linked_list = []

    for item in linked_list:
        src_path = os.path.join(config, github_repo, item)
        dest_path = os.path.join(shared_folder, os.path.basename(item))
        if not os.path.exists(src_path):
            print(f"Source {item} does not exist in repo.")
        else:
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path) if os.path.isdir(dest_path) else os.remove(dest_path)
            shutil.copytree(src_path, dest_path) if os.path.isdir(src_path) else shutil.copy2(src_path, dest_path)
            print(f"Applied {item} to shared folder.")

def info(f):
    print(f"Welcome, {github_name}")
    print("Welcome to CreateSync. To get started, go to:")
    print(docurl, "\n")
    print(f"VERSION {app_version}")

    options = {
        "false": ["Clone repo", "Sync from cloud", "Sync to cloud", "Edit config (COMING SOON)", "Help", "Exit"],
        "true": ["Sync from cloud", "Sync to cloud", "Edit config (COMING SOON)", "Add files, dir", "Apply", "Help", "RESET TO DEFAULT", "Exit"]
    }

    for i, opt in enumerate(options[f], 1):
        print(f"[{i}] {opt}")

    userinput = input("Select an option: ").strip().upper()
    return userinput if userinput in [str(i) for i in range(1, len(options[f]) + 1)] else info(f)

def optioncheck(option, f):
    clear_screen()

    if option == "1":
        if f == "false":
            subprocess.run(["python3" if os.name != "nt" else "python", "clone.py"])
        else:
            print("Syncing from cloud...")
            sync_from_cloud()
            wait(2)
            optioncheck(info(f), f)
    elif option == "2":
        print("Syncing to cloud...")
        wait(2)
        optioncheck(info(f), f)
    elif option == "3":
        print("Editing config... (Feature in progress)")
        wait(2)
        optioncheck(info(f), f)
    elif option == "4":
        print("LINK DIR/FILE")
        file_input = input("Copy the directory and paste it here: ")
        file_path = os.path.join(config, github_repo, "scripts", "linked.txt")
        ensure_file_exists(file_path)
        with open(file_path, "r+") as txt_file:
            content = txt_file.read().strip()
            new_content = merge_lists(content, file_input)
            txt_file.seek(0)
            txt_file.truncate()
            txt_file.write(new_content)
        optioncheck(info(f), f)
    elif option == "5":
        print("Applying linked directories to shared folder...")
        apply_linked()
        wait(3)
        optioncheck(info(f), f)
    elif option == "6":
        print(f"Go to {docurl} for help!")
        wait(3)
        optioncheck(info(f), f)
    elif option == "7" and f == "true":
        userinput = input("Are you sure you want to reset? It may break the code. [Y/N]").strip().upper()
        if userinput == "Y":
            with open(info_file, "w") as f:
                f.write("false")
        clear_screen()
        exit()

optioncheck(info(ink), ink)
