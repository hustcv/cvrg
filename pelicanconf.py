#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'hustcv'
SITENAME = u'Computer Vision Reading Group'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = u'ch'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = '/home/dumin/tmp/blue-penguin'

# all the following settings are *optional*

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'
NOTES_URL		   = 'notes'
NOTES_SAVE_AS      = 'notes/index.html'
# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
        ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
        ('Tags', TAGS_URL, TAGS_SAVE_AS),
        ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
        ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
		('Notes',NOTE_URL,NOTE_SAVE_AS),
        )
# additional menu items
MENUITEMS = (
        ('GitHub', 'https://github.com/hustcv'),
        )
