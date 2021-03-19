# @Time:  2021/3/19 23:20
# @Author: 小烦人
# @File:  main.py
# coding=utf-8


import unittest, os
from common.html_reporter import GenerateReport

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__), "tests"),
                                                pattern='*.py', top_level_dir=os.path.dirname(__file__))
    html_report = GenerateReport()
    html_report.generate_report(suite)