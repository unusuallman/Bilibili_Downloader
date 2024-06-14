from utils.bilibili_spider import Bilibili_Spider
from pathlib import Path
import openpyxl

def core(*args):
    id = args[0]
    save_dir = args[1]
    time = args[2]
    bilibili_spider = Bilibili_Spider(id, save_dir, time)
    bilibili_spider.get()


def load_xlsx():
    xlsx_files = list(Path('.').rglob('*.xlsx'))
    for xlsx_file in xlsx_files:
        wb = openpyxl.load_workbook(xlsx_file)
        sheet = wb['Sheet1']
        
