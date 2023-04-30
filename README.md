# Git-Fork-Sync-Py
GitHub Fork Sync is a Python script that automatically updates your forked repositories on GitHub by syncing them with their upstream counterparts. The script checks for changes in the original repositories and updates the corresponding forks accordingly. It supports multiple repositories and directly uses the GitHub API.

# GitHub Fork Sync

GitHub Fork Sync is a Python script that automatically updates your forked repositories on GitHub by syncing them with their upstream counterparts. The script checks for changes in the original repositories and updates the corresponding forks accordingly. It supports multiple repositories and uses the GitHub API for seamless integration.

## Features

- Automatically sync forked repositories with their upstream counterparts
- Support for multiple repositories
- Utilizes GitHub API for efficient updates
- Easy configuration using environment variables

## Prerequisites

- Python 3.8+
- A GitHub account with forked repositories
- A [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with "repo" scope

## Dependencies

The script requires the following Python packages:

- `requests`
- `python-dotenv`

You can install them using the following command:

```
pip install requests python-dotenv
