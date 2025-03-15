from dotenv import load_dotenv
import os
import git
import subprocess
load_dotenv()
ink = open("./CONFIG/info.txt")

GITHUBTOKEN = os.getenv('GITHUBTOKEN')
GITHUBUSER = os.getenv('GITHUBUSER')
GITHUBNAMEREPO = os.getenv('GITHUBNAMEREPO')

if not GITHUBTOKEN or not GITHUBUSER or not GITHUBNAMEREPO:
    print(f"Please read the {docurl} to continue to use Create Snyc!")
    exit(1)

REPO_URL = f"https://{GITHUBUSER}:{GITHUBTOKEN}@github.com/{GITHUBUSER}/{GITHUBNAMEREPO}.git"

print("Cloning GitHub repo...")
try:
    git.Repo.clone_from(REPO_URL, "./CONFIG")
    print("Clone successful!")
except Exception as e:
    print(f"Error cloning repository: {e}")
ink.write("true")
subprocess.run("python3 selectmenu.py")
subprocess.run("python selectmenu.py")
