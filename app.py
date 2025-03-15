from dotenv import load_dotenv
import os
import git

load_dotenv()
app_version = "1.0.0"
docurl = "[WIP]"
GITHUBTOKEN = os.getenv('GITHUBTOKEN')
GITHUBUSER = os.getenv('GITHUBUSER')
GITHUBLINKURL = os.getenv('GITHUBLINKURL')

if not GITHUBTOKEN or not GITHUBUSER or not GITHUBLINKURL:
    print(f"Please read the {docurl} to continue to use Create Snyc!")
    exit(1)

REPO_URL = f"https://{GITHUBUSER}:{GITHUBTOKEN}@github.com/{GITHUBUSER}/{GITHUBLINKURL}.git"

print("Have you use CreateSync before? [Y/N]")
userinput = input("")
if userinput == "Y" :
    print(f"Read {docurl} to Sync your data")
    userinput =input("")
elif userinput == "N" :
    print("Cloning GitHub repo...")
    try:
        git.Repo.clone_from(REPO_URL, "./CONFIG")
        print("Clone successful!")
    except Exception as e:
        print(f"Error cloning repository: {e}")
else :
    print(f"Please read {docurl} to use create sync")