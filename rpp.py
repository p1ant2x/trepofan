import os
import git
import requests

from git import Repo
username = input("Please enter your Github account name: ")
response = requests.get("https://api.github.com/users/" + username + "/repos")
repositories =  response.json()

for x in range(1700,1800):
    os.mkdir("my_repositories/" + str(x))
    for repo in repositories:
	    command = git.Git().clone(repo["clone_url"], "my_repositories/" + str(x) + repo["name"], recursive=True)
	    r = Repo("my_repositories/" + str(x) + repo["name"])
	    r.create_remote('originate', repo["clone_url"])
	    print(command + "one sec")