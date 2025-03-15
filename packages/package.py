# package.py
import git 
import json

def logo() :
    print("┏┓         ┏┓     ")
    print("┃ ┏┓┏┓┏┓╋┏┓┗┓┓┏┏┓┏")
    print("┗┛┛ ┗ ┗┻┗┗ ┗┛┗┫┛┗┗")
    print("              ┛   ")
    print("-----------------------------")

def git_pull(repo,repo_path):
    try:
        repo = git.Repo(repo_path)
        repo.remote().pull()
        print("Pulled latest changes.")
    except Exception as e:
        print(f"Error pulling: {e}")

def git_push(repo,repo_path,commit_message):
    try:
        repo = git.Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        repo.remote().push()
        print("Changes pushed successfully.")
    except Exception as e:
        print(f"Error pushing: {e}")



def merge_lists(list1, list2):
    """Merges two lists."""
    return list1 + list2

def read_list(lst, index):
    """Reads a value at a specific index from a list."""
    return lst[index] if 0 <= index < len(lst) else None