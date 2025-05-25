import os
from github import Github
import pandas as pd

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

GITHUB_KEY = os.getenv("GITHUB_KEY")

g = Github(GITHUB_KEY)

repositories = ["mumuvrf/CoDes-App", "marcosnovaesq/qual_a_boua",
                "mumuvrf/PyGameRPG", "apracadev/praca", "talesitf/cautious-enigma",
                "talesitf/Codes-221", "talesitf/DataDuner", 
                "arcotech-services/data-analysis-rag-experiments"]

commit_data = [["code", "message", "is_code_related"]]

for repo_name in repositories:
    print(f"Opa! Tô pegando commits do repositório: {repo_name}")
    repo = g.get_repo(repo_name)
    for commit in repo.get_commits():
        message = commit.commit.message
        full_commit = repo.get_commit(commit.sha)
        code = ""
        for file in full_commit.files:
            filename = file.filename
            patch = file.patch
            code += f"\nFile:{filename}\nCode modifications:\n{patch}\n"
        commit_data.append([code, message])

df = pd.DataFrame(commit_data)
df.to_excel("data.xlsx")