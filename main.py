"""
爬虫启动脚本
"""
import os
import sys

from scrapy.cmdline import execute

# 将当前项目目录追加到python搜索模块路径
sys.path.append(os.path.abspath(__file__))

# 执行命令启动爬虫
execute(['scrapy','crawl','jobbole'])