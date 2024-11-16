

AUTHOR          = 'raja'
SITENAME        = 'My Notes'


# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/<yourusername>/"),
    ("LinkedIn", "<linkedin handle>"),
)

######## Advanced Settings (not recommended to to edited) #############

import os
from git import Repo

# Get the current repository name dynamically
repo = Repo(os.getcwd())
FOLDER_NAME = os.path.basename(repo.working_dir)

# FOLDER_NAME     = "sigpytest"

# siteurl format: 'https://<username/orgname>.github.io/<reponame>'
SITEURL         = f'https://tactlabs.github.io/{FOLDER_NAME}'


OUTPUT_PATH     = 'docs'
PATH            = "content"
TIMEZONE        = 'America/Toronto'
DEFAULT_LANG    = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM               = None
CATEGORY_FEED_ATOM          = None
TRANSLATION_FEED_ATOM       = None
AUTHOR_FEED_ATOM            = None
AUTHOR_FEED_RSS             = None

DEFAULT_PAGINATION          = 10

# Uncomment following line if you want document-relative URLs when developing
# Use SITEURL for absolute paths; RELATIVE_URLS is typically for local preview
RELATIVE_URLS = False

THEME               = 'themes/zurb-F5-basic'

IGNORE_FILES        = [".*", "*.swp", "*~"]  # Ignore hidden files and temporary files

