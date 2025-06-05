import os
from github import Github
from deep_translator import GoogleTranslator
import pandas as pd

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

GITHUB_KEY = os.getenv("GITHUB_KEY")

g = Github(GITHUB_KEY)

repositories = ["mumuvrf/CoDes-App", "marcosnovaesq/qual_a_boua",
                "mumuvrf/PyGameRPG", "apracadev/praca", "talesitf/cautious-enigma",
                "talesitf/Codes-221", "talesitf/DataDuner", 
                "pedronery07/Pygame-2022.2", "antoniolma/PyGameDessoft",
                "raulikeda/OpenManus"]

commit_data = [["code", "message", "message_english", "is_code_related"]]

for repo_name in repositories:
    print(f"Opa! Tô pegando commits do repositório: {repo_name}")
    repo = g.get_repo(repo_name)
    for commit in repo.get_commits():
        message = commit.commit.message
        message_english = GoogleTranslator(source='auto', target='en').translate(message)
        full_commit = repo.get_commit(commit.sha)
        code = ""
        for file in full_commit.files:
            filename = file.filename
            patch = file.patch
            code += f"\nFile:{filename}\nCode modifications:\n{patch}\n"
        commit_data.append([code, message, message_english])

df = pd.DataFrame(commit_data)
df.to_excel("data.xlsx")