import requests
import gzip


def loadRaw(name):
    return gzip.open(f'./{name}.eden', 'rb').read()
