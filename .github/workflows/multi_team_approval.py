import os
import sys
from github import Github

# Replace with your GitHub token
github_token = os.environ['GITHUB_TOKEN']
repo_owner = "VATGER-Nav"
repo_name = "aliases"
pr_number = int(os.environ['GITHUB_EVENT_NUMBER'])
required_teams = ["EDGG", "EDMM", "EDWW"]

def main():
    # Initialize the GitHub API client
    g = Github(github_token)
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    pr = repo.get_pull(pr_number)

    # Get the teams that have approved the PR
    approved_teams = []
    for review in pr.get_reviews():
        if review.user.type == "Team" and review.state == "APPROVED":
            approved_teams.append(review.user.login)

    # Check if there are at least three different approved teams
    unique_approved_teams = set(approved_teams)
    if len(unique_approved_teams) < 3:
        print("Not enough approvals from distinct teams.")
        sys.exit(1)

if __name__ == "__main__":
    main()
