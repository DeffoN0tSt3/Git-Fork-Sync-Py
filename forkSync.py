import os
import requests
from github import Github
from dotenv import load_dotenv

def load_env_vars():
    load_dotenv()
    return os.getenv("GITHUB_ACCESS_TOKEN"), os.getenv("REPOSITORIES")

def get_repo_data(g, repo_name):
    user = g.get_user()
    repo = user.get_repo(repo_name)
    head_branch = repo.get_branch("master")
    upstream = repo.parent
    base_branch = upstream.get_branch("master")
    return head_branch, base_branch

def update_repo(repo_name, access_token):
    g = Github(access_token)
    try:
        repo = g.get_user().get_repo(repo_name)
        head_branch = repo.get_branch("master")
        upstream = repo.parent
        base_branch = upstream.get_branch("master")
        if head_branch.commit.sha != base_branch.commit.sha:
            print(f"Updating {repo_name}...")
            url = f'https://api.github.com/repos/{repo.full_name}/git/refs/heads/{head_branch.name}'
            payload = {"sha": base_branch.commit.sha, "force": True}
            headers = {'Authorization': f'token {access_token}', 'Accept': 'application/vnd.github+json'}
            response = requests.patch(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f"{repo_name} updated successfully!")
            else:
                print(f"Error updating {repo_name}: {response.status_code} {response.json()}")
        else:
            print(f"No changes detected in {repo_name}.")
    except Exception as e:
        print(f"Error: {e}")
        
def main():
    access_token, repositories_str = load_env_vars()
    repositories = repositories_str.split(',')

    for repo_name in repositories:
        update_repo(repo_name.strip(), access_token)

if __name__ == "__main__":
    main()
