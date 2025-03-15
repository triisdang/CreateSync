# package.py
import git
import json
import os
def logo():
    print("┏┓         ┏┓     ")
    print("┃ ┏┓┏┓┏┓╋┏┓┗┓┓┏┏┓┏")
    print("┗┛┛ ┗ ┗┻┗┗ ┗┛┗┫┛┗┗")
    print("              ┛   ")
    print("-----------------------------")
def git_pull(repo, repo_path):
    try:
        repo = git.Repo(repo_path)
        repo.remote().pull()
        print("Pulled latest changes.")
    except Exception as e:
        print(f"Error pulling: {e}")
def git_push(repo, repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        repo.remote().push()
        print("Changes pushed successfully.")
    except Exception as e:
        print(f"Error pushing: {e}")
def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}. Creating it now...")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        open(file_path, "w").close()
def merge_lists(list1, list2):
    return list1 + list2
def read_list(lst, index):
    return lst[index] if 0 <= index < len(lst) else None
