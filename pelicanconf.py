#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dylan Campbell'
SITENAME = 'Dylan Campbell'
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/profile.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

SITETITLE = AUTHOR
SITESUBTITLE = 'Software Developer'

MAIN_MENU = True

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'English'

THEME = 'pelican-themes/flex'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IPYNB_FIX_CSS= True

# MD_EXTENSIONS = ['extra']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sidebar
SIDEBAR_DIGEST = 'Software Developer'


DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('Blog', SITEURL),)

# Blogroll
# LINKS = (('Nick\'s Blog','https://nickrcasteen.github.io/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/dylancharlescampbell'),
          ('github', 'https://github.com/dcc023'),
          ('facebook', 'https://www.facebook.com/campbelldylancharles')
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
