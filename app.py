from dotenv import load_dotenv
import os

load_dotenv()

GITHUBTOKEN = os.getenv('GITHUBTOKEN')
GITHUBUSER = os.getenv('GITHUBUSER')
GITHUBLINKURL = os.getenv('GITHUBLINKURL')


if GITHUBLINKURL == "" or GITHUBTOKEN == "" or GITHUBUSER == "" :
    print("Please read the README.md to continue")
else :
    print("test")