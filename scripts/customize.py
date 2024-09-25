#!/usr/bin/env python3

# This script is run by the user using `make customize` after the repository
# is cloned. If you are reading this because `make customize` failed,
# skip down to the section headed "INITIALIZATION STEPS".

from sh import git
import datetime
import re
import sys
from urllib.parse import quote
import subprocess
import requests

BASE_OWNER = "googlefonts"
BASE_REPONAME = "googlefonts-project-template"
DUMMY_URL = "https://yourname.github.io/your-font-repository-name"
LATEST_OFL = "https://raw.githubusercontent.com/googlefonts/googlefonts-project-template/main/OFL.txt"


def repo_url(owner, name):
    return f"https://github.com/{owner}/{name}"


def web_url(owner, name):
    return f"https://{owner}.github.io/{name}"


def raw_url(owner, name):
    return f"https://raw.githubusercontent.com/{owner}/{name}"


def lose(msg, e=None):
    print(msg)
    print("You will need to do the initialization steps manually.")
    print("Read scripts/customize.py for more instructions how to do this.")
    if e:
        print(
            "\nHere's an additional error message which may help diagnose the problem."
        )
        raise e
    sys.exit(1)


try:
    my_repo_url = git.remote("get-url", "origin")
except Exception as e:
    lose("Could not use git to find my own repository URL", e)

m = re.match(r"(?:https://github.com/|git@github.com:)(.*)/(.*)/?", str(my_repo_url))
if not m:
    lose(
        f"My git repository URL ({my_repo_url}) didn't look what I expected - are you hosting this on github?"
    )

owner, reponame = m[1], m[2]

if owner == BASE_OWNER and reponame == BASE_REPONAME:
    print("I am being run on the upstream repository; don't do that")
    sys.exit()

# INITIALIZATION STEPS

# First, the README file contains URLs to pages in the `gh-pages` branch of the
# repo. When initially cloned, these URLs will point to the
# googlefonts/Unified-Font-Repository itself. But downstream users want links
# and badges about their own font, not ours! So any URLs need to be adjusted to
# refer to the end user's repository.

# We will also pin the dependencies so future builds are reproducible.

readme = open("README.md").read()
ghpages_url = web_url(owner, reponame)
project_url = repo_url(owner, reponame)

print("Fixing URLs:", web_url(BASE_OWNER, BASE_REPONAME), "->", ghpages_url)

readme = readme.replace(web_url(BASE_OWNER, BASE_REPONAME), ghpages_url)
# In the badges, the URLs to raw.githubusercontent.com are URL-encoded as they
# are passed to shields.io.
readme = readme.replace(
    quote(raw_url(BASE_OWNER, BASE_REPONAME), safe=""),
    quote(raw_url(owner, reponame), safe=""),
)

print("Fixing URLs:", DUMMY_URL, "->", ghpages_url)
readme = readme.replace(f"`{DUMMY_URL}`", ghpages_url)

with open("README.md", "w") as fh:
    fh.write(readme)

git.add("README.md")

# Fix the OFL
year = datetime.date.today().year
title = reponame.title()
copyright = f"Copyright {year} The {title} Project Authors ({project_url})\n"
print("Fetching the latest OFL..")
ofl = requests.get(LATEST_OFL).text.splitlines()
print("Writing an OFL for you")
print(copyright)
with open("OFL.txt", "w") as fh:
    fh.write(copyright)
    fh.write("\n".join(ofl[1:]))

git.add("OFL.txt")

# Pin the dependencies
print("Pinning dependencies")
dependencies = subprocess.check_output(["pip", "freeze"])
with open("requirements.txt", "wb") as dependency_file:
    dependency_file.write(dependencies)
git.add("requirements.txt")

# Did anything change?
result = git.status("--porcelain")
if any(line.startswith("M ") for line in result.splitlines()):
    git.commit("-m", "Customize repository")

    print("Pushing changes to GitHub")
    git.push()
else:
    print("Nothing changed, no need to push")
