# clone.py
from dotenv import load_dotenv
import os
import git
import subprocess
from time import sleep as wait
from packages.package import *

load_dotenv()
config = "../config"
CONFIG_PATH = f"{config}info.txt"
GITHUBTOKEN = os.getenv('GITHUBTOKEN')
GITHUBUSER = os.getenv('GITHUBUSER')
GITHUBNAMEREPO = os.getenv('GITHUBNAMEREPO')
docurl = "https://github.com/triisdang/CreateSync/wiki"

if not GITHUBTOKEN or not GITHUBUSER or not GITHUBNAMEREPO:
    print(f"Please read the {docurl} to continue using CreateSync!")
    exit(1)

REPO_URL = f"https://{GITHUBUSER}:{GITHUBTOKEN}@github.com/{GITHUBUSER}/{GITHUBNAMEREPO}.git"

print("Cloning GitHub repo...")

try:
    os.makedirs(f"{config}/{GITHUBNAMEREPO}", exist_ok=True)
except PermissionError:
    print(f"Permission denied: Unable to create '{GITHUBNAMEREPO}'.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

wait(2)

try:
    git.Repo.clone_from(REPO_URL, f"{config}/{GITHUBNAMEREPO}")
    print("Clone successful!")
    wait(4)
except Exception as e:
    print(f"Error cloning repository: {e}")
    exit(1)

with open(CONFIG_PATH, "w") as ink:
    ink.write("true")

os.makedirs(f"{config}/{GITHUBNAMEREPO}/scripts", exist_ok=True)

with open(f"{config}/{GITHUBNAMEREPO}/scripts/info.txt", "w") as f:
    f.write("test")

with open(f"{config}/{GITHUBNAMEREPO}/scripts/linked.txt", "w") as f:
    f.write("[]")

git_push(GITHUBNAMEREPO, f"CONFIG/{GITHUBNAMEREPO}", "Update.")

selectscript = os.path.join(os.path.dirname(os.path.abspath(__file__)), "selectmenu.py")
subprocess.run(["python3" if os.name != "nt" else "python", selectscript])