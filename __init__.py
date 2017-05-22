# !/usr/bin/python
# -*- coding: UTF-8 -*-
import url_manager
import html_downloader
import html_outputer
import html_parser


class SpiderMain(object):
    # initiate all objects
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url_manager
        self.downloader = html_downloader.HtmlDownloader()  # html_downloader
        self.parser = html_parser.HtmlParser()  # html_parser
        self.outputer = html_outputer.HtmlOutputer()  # html_outputer

    def craw(self, root_url):
        # put root_url in url_manager
        self.urls.add_main_url(root_url)


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/行政区划"  # this link is the entrance of provinces in china.
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # begin scraping
