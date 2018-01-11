#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bhaskar Kamble'
SITENAME = 'Random Forests'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#RELATIVE_URLS = False

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

#THEME = "./pelican-themes/waterspill"

# Title menu options
MENUITEMS = (('About', 'https://bhaskarkamble.com'),('Archives', "/archives.html"))
#             ('Archives', 'bhaskar-kamble.github.io/archives.html'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/baski170182'),
          ('YouTube', 'https://www.youtube.com/channel/UCuC--7f00jwHWAXix-66oUg'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

