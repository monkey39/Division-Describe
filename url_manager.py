#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_main_url(self, url):
        try:
            html=urlopen(url)
        except HTTPError as e:
            print("there is a HTTPError.")
            return None
        try:
            bsObj=BeautifulSoup(html.read())
            title=bsObj.body.h1
        except AttributeError as e:
            print("there is a AttributeError.")
            return None
        return title
