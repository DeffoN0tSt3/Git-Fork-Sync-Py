# Git-Fork-Sync-Py
GitHub Fork Sync is a Python script that automatically updates your forked repositories on GitHub by syncing them with their upstream counterparts. The script checks for changes in the original repositories and updates the corresponding forks accordingly. It supports multiple repositories and directly uses the GitHub API.

# GitHub Fork Sync

GitHub Fork Sync is a Python script that automatically updates your forked repositories on GitHub by syncing them with their upstream counterparts. The script checks for changes in the original repositories and updates the corresponding forks accordingly. It supports multiple repositories and uses the GitHub API for seamless integration.

## Features

- Automatically sync forked repositories with their upstream counterparts
- Support for multiple repositories
- Utilizes GitHub API for efficient updates
- Easy configuration using environment variables

## Usage

Clone the repo:
```
git clone https://github.com/DeffoN0tSt3/Git-Fork-Sync-Py.git
```
```
cd Git-Fork-Sync-Py
```

Edit .env 
- add repo name(s) comma separated 
- add your Git access token


``` py forkSync.py```

The script will automatically update the specified forked repositories on GitHub by syncing them with their upstream counterparts.


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
```

### License

This code is licensed under the MIT License - see the LICENSE file for details.

### Disclaimer

Please use this script responsibly and do not use it to create unnecessary load on GitHub's servers. The author is not responsible for any misuse or any damages resulting from the use of this script.
