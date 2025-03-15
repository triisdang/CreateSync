from dotenv import load_dotenv
import os
import subprocess


app_version = "1.0.0"
docurl = "[WIP]"
load_dotenv()
github_name = os.getenv('GITHUBUSER')

subprocess.run("clear")

print("Hello!")
print("Wellcome to CreateSync. To get started, goto")
print(docurl)
for i in range(2) :
    print()

print("[1] Sync to cloud")
print("[2] Sync from cloud")