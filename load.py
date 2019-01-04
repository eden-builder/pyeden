from helper import loadRaw
from struct import Struct
import pprint
pp = pprint.PrettyPrinter(indent=4)


def parseDict(d):
    for k in d.copy():
        if type(d[k]) is bytes:
            d[k] = d[k][:d[k].find(0)].decode('utf-8')
        if '.' in k:
            p, c = k.split('.')
            if p not in d:
                d[p] = {}
            d[p][c] = d[k]
            del d[k]
    return d


class NamedStruct(Struct):
    def __init__(self, format='i', fields=('int',), offset=0):
        super(NamedStruct, self).__init__(format)
        self.fields = fields
        self.offset = offset

    def load(self, raw):
        return parseDict(dict(zip(self.fields, self.unpack(raw[self.offset:self.offset + self.size]))))


header = NamedStruct('i fff fff f Q 50s i 36s 16s i 192s',
                     ('level_seed', 'pos.x', 'pos.y', 'pos.z', 'home.x', 'home.y', 'home.z', 'yaw', 'directory_offset', 'name', 'version', 'hash', 'skycolors', 'goldencubes', 'reserved'))


def bint(b):
    return int.from_bytes(b, byteorder='little')


raw = loadRaw('1541108087')
h = header.load(raw)
pprint.pprint(h)
