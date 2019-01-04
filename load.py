import ctypes
import numpy as np
from helper import loadRaw

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def mapMem(src, obj, start=0):
    ctypes.memmove(ctypes.byref(
        obj), src[start:ctypes.sizeof(obj)], ctypes.sizeof(obj))


class BaseStructure(ctypes.Structure):
    @classmethod
    def fromBinary(cls, raw, start=0):
        obj = cls()
        mapMem(raw, obj, start)
        return obj

    def getdict(self):
        return dict((f, getattr(self, f).getdict() if hasattr(t, '_fields_') else getattr(self, f).decode('ascii') if type(getattr(self, f)) is bytes else getattr(self, f)) for f, t in self._fields_)

    def getArray(self):
        return np.array(self)


class Color(BaseStructure):
    _fields_ = [('r', ctypes.c_int),
                ('g', ctypes.c_int),
                ('b', ctypes.c_int),
                ('a', ctypes.c_int)]


class Vector(BaseStructure):
    _fields_ = [('x', ctypes.c_float),
                ('y', ctypes.c_float),
                ('z', ctypes.c_float)]


class WorldFileHeader(BaseStructure):
    _fields_ = [('level_seed', ctypes.c_int),
                ('pos', Vector),
                ('home', Vector),
                ('yaw', ctypes.c_float),
                ('directory_offset', ctypes.c_ulonglong),
                ('name', ctypes.c_char * 50),
                ('version', ctypes.c_int),
                ('hash', ctypes.c_char * 36),
                ('skycolors', Color),
                ('goldencubes', ctypes.c_int),
                ('reserved', ctypes.c_char * 192)]


class ColumnIndex(BaseStructure):
    _fields_ = [('x', ctypes.c_int),
                ('z', ctypes.c_int),
                ('chunk_offset', ctypes.c_ulonglong)]


class ChunkHeader(BaseStructure):
    _fields_ = [('n_vertices', ctypes.c_int)]


class Chunk(BaseStructure):
    _fields_ = [('blocks', ((ctypes.c_byte*16)*16)*16),
                ('colors', ((ctypes.c_byte*16)*16)*16)]


class Column(BaseStructure):
    _fields_ = [('chunks', Chunk*4)]

    def getBlocks(self):
        return np.concatenate(self.getArray()['chunks'][...]['blocks'], axis=2)


def showCube(cube):
    x, y, z = cube.nonzero()
    c = cube[x, y, z]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    pnt3d = ax.scatter(x, y, z, c=c)
    cbar = plt.colorbar(pnt3d)
    cbar.set_label("Values (units)")
    plt.show()


def main():
    raw = loadRaw('1541108087')
    header = WorldFileHeader.fromBinary(raw, 0)

    col = Column.fromBinary(raw, 192)

    cube = col.getBlocks()
    cube[cube > 10] = 1  # for better visibility
    showCube(cube)


if __name__ == '__main__':
    main()
