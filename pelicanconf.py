#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dylan Campbell'
SITENAME = 'Dylan Campbell'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'English'

THEME = 'pelican-themes/pelican-blue'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sidebar
SIDEBAR_DIGEST = 'Software Developer'

FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('Blog', SITEURL),)

# Blogroll
LINKS = (('Nick\'s Blog','https://nickrcasteen.github.io/'),
	     )

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/dylancharlescampbell'),
          ('github', 'https://github.com/dcc023'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
