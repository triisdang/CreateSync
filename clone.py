from dotenv import load_dotenv
import os
import git
import subprocess
from time import sleep as wait

load_dotenv()

CONFIG_PATH = "./CONFIG/info.txt"

GITHUBTOKEN = os.getenv('GITHUBTOKEN')
GITHUBUSER = os.getenv('GITHUBUSER')
GITHUBNAMEREPO = os.getenv('GITHUBNAMEREPO')
docurl = "[WIP]"

if not GITHUBTOKEN or not GITHUBUSER or not GITHUBNAMEREPO:
    print(f"Please read the {docurl} to continue using CreateSync!")
    exit(1)

REPO_URL = f"https://{GITHUBUSER}:{GITHUBTOKEN}@github.com/{GITHUBUSER}/{GITHUBNAMEREPO}.git"

print("Cloning GitHub repo...")

try:
    os.mkdir(f"./CONFIG/{GITHUBNAMEREPO}")
except FileExistsError:
    print(f"Directory '{GITHUBNAMEREPO}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{GITHUBNAMEREPO}'.")
except Exception as e:
    print(f"An error occurred: {e}")

wait(2)

try:
    git.Repo.clone_from(REPO_URL, f"./CONFIG/{GITHUBNAMEREPO}")
    print("Clone successful!")
    wait(4)
except Exception as e:
    print(f"Error cloning repository: {e}")

with open(CONFIG_PATH, "w") as ink:
    ink.write("true")

subprocess.run(["python3", "selectmenu.py"])
