# coding:utf-8
"""
将给定的list内容，写入excel
"""
from openpyxl import Workbook


def gen_xls(title=[], lis=[]):
    wb = Workbook()
    ws = wb.active  # 激活worksheet
    ws.append(title)
    for l1 in lis:
        ws.append(l1)
    return wb
