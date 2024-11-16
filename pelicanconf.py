

FOLDER_NAME     = "sigpytest"

# siteurl format: 'https://<username/orgname>.github.io/<reponame>'
SITEURL         = f'https://tactlabs.github.io/{FOLDER_NAME}'

AUTHOR          = 'raja'
SITENAME        = 'My Notes'

OUTPUT_PATH     = 'docs'

PATH            = "content"
TIMEZONE        = 'Europe/Rome'
DEFAULT_LANG    = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM               = None
CATEGORY_FEED_ATOM          = None
TRANSLATION_FEED_ATOM       = None
AUTHOR_FEED_ATOM            = None
AUTHOR_FEED_RSS             = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/<yourusername>/"),
    ("LinkedIn", "<linkedin handle>"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# Use SITEURL for absolute paths; RELATIVE_URLS is typically for local preview
RELATIVE_URLS = False

THEME               = 'themes/zurb-F5-basic'

IGNORE_FILES        = [".*", "*.swp", "*~"]  # Ignore hidden files and temporary files

