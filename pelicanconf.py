#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'odoomaster'
SITENAME = u'Odoo Master Blog'
SITEURL = ''
SITELOGO = 'https://avatars3.githubusercontent.com/u/4207333?v=3&s=140'
PATH = 'content'
SITETITLE = 'Hoang, Diep Huu'
SITESUBTITLE = 'Share Odoo Experience'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#INKS = (('Pelican', 'http://getpelican.com/'),
#        ('Python.org', 'http://python.org/'),
#        ('Jinja2', 'http://jinja.pocoo.org/'),
#        ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/hoang-diep-huu-061b5769'),
          ('github', 'https://github.com/anothingguy'),
          ('twitter', 'https://twitter.com/hoangrc'),
          ('rss', '//blog.odoomaster.com/feeds/all.atom.xml'))
DEFAULT_PAGINATION = 10

THEME = "./pelican-themes/Flex"

COPYRIGHT_YEAR = 2016

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'post_stats']

# Disqus
DISQUS_SITENAME = "blog-odoomaster-com"

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
                          ('Tags', '/tags.html'),)
                          

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
