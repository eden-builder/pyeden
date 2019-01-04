import requests
import gzip

BASE = 'edengame.net'
APP_BASE_URL = f'http://app.{BASE}'
FILES_BASE_URL = f'http://files.{BASE}'
UPLOAD_URL = f'{APP_BASE_URL}/upload2.php'
REPORT_URL = f'{APP_BASE_URL}/report.php'
POPULAR_URL = f'{FILES_BASE_URL}/popularlist.txt'


def DOWNLOAD_MAP(id): return f'{FILES_BASE_URL}/{id}.eden'


def DOWNLOAD_MAP_IMAGE(id): return f'{FILES_BASE_URL}/{id}.eden.png'


def downloadRaw(id):
    return requests.get(DOWNLOAD_MAP(id)).content


def loadRaw(id):
    return gzip.open(f'./{id}.eden', 'rb').read()
