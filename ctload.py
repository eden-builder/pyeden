import ctypes
from helper import loadRaw


class BaseStructure(ctypes.Structure):
    def getdict(self):
        return dict((f, getattr(self, f).getdict() if hasattr(t, '_fields_') else getattr(self, f).decode('ascii') if type(getattr(self, f)) is bytes else getattr(self, f)) for f, t in self._fields_)


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


raw = loadRaw('1541108087')
header = WorldFileHeader()
ctypes.memmove(ctypes.byref(header), raw, ctypes.sizeof(header))
