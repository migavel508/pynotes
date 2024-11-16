

FOLDER_NAME     = "sigpytest"

# siteurl format: 'https://<username/orgname>.github.io/<reponame>'
SITEURL         = f'https://tactlabs.github.io/{FOLDER_NAME}'

AUTHOR          = 'raja'
SITENAME        = 'My Notes'
SITEURL         = ""

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
    ("GitHub", "https://github.com/tactlabs/"),
    ("LinkedIn", "https://linkedin.com"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# Use SITEURL for absolute paths; RELATIVE_URLS is typically for local preview
RELATIVE_URLS = False

THEME               = 'themes/zurb-F5-basic'

# URL settings (include folder name in URLs)
ARTICLE_URL = f'{FOLDER_NAME}/{{slug}}.html'
ARTICLE_SAVE_AS = '{slug}.html'

PAGE_URL = f'{FOLDER_NAME}/{{slug}}.html'
PAGE_SAVE_AS = '{slug}.html'

CATEGORY_URL = f'{FOLDER_NAME}/category/{{slug}}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

TAG_URL = f'{FOLDER_NAME}/tag/{{slug}}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'  # Keep archives in root
