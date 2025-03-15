from dotenv import load_dotenv
import os
import git
import subprocess
load_dotenv()
ink = open("./CONFIG/info.txt")

GITHUBTOKEN = os.getenv('GITHUBTOKEN')
GITHUBUSER = os.getenv('GITHUBUSER')
GITHUBLINKURL = os.getenv('GITHUBLINKURL')

if not GITHUBTOKEN or not GITHUBUSER or not GITHUBLINKURL:
    print(f"Please read the {docurl} to continue to use Create Snyc!")
    exit(1)

REPO_URL = f"https://{GITHUBUSER}:{GITHUBTOKEN}@github.com/{GITHUBUSER}/{GITHUBLINKURL}.git"

print("Cloning GitHub repo...")
try:
    git.Repo.clone_from(REPO_URL, "./CONFIG")
    print("Clone successful!")
except Exception as e:
    print(f"Error cloning repository: {e}")
ink.write("true")
subprocess.run("python3 selectmenu.py")
subprocess.run("python selectmenu.py")
