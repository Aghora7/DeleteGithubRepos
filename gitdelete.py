import requests

username = 'USER_NAME' # your account name or org name which you want delete files for
token = 'DUMMY_TOKEN_PUT_YOUR_TOKEN'  # Generate a personal access token from GitHub

headers = {
    'Authorization': f'token {token}',
}

# Fetch the list of repositories
url = f'https://api.github.com/user/repos'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        repo_name = repo['name']
        delete_url = f'https://api.github.com/repos/{username}/{repo_name}'
        delete_response = requests.delete(delete_url, headers=headers)

        if delete_response.status_code == 204:
            print(f'Repository {repo_name} deleted successfully')
        else:
            print(f'Failed to delete repository {repo_name}. Status code: {delete_response.status_code}')
            print(delete_response.text)
else:
    print(f'Failed to fetch repositories. Status code: {response.status_code}')
    print(response.text)
