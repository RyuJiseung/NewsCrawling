# -*- coding: utf-8 -*-

# Scrapy settings for newscrawling project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'newscrawling'

SPIDER_MODULES = ['newscrawling.spiders']
NEWSPIDER_MODULE = 'newscrawling.spiders'
LOG_LEVEL='ERROR'

ITEM_PIPELINES = {'newscrawling.pipelines.CsvPipeline':300, }


