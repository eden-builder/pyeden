from helper import loadRaw
from cffi import FFI

ffi = FFI()

ffi.cdef('''
struct Vector{
    float    x;
    float    y;
    float    z;
};
typedef struct Vector Vector;

typedef struct{
    int level_seed;
    Vector pos;
    Vector home;
    float yaw;
    unsigned long long directory_offset;
    char name[50];
    int version;
    char hash[36];
    unsigned char skycolors[16];
    int goldencubes;
    char reserved[192];
}WorldFileHeader;
typedef struct{
    int x, z;
    unsigned long long chunk_offset;
}ColumnIndex;
typedef struct{
    int n_vertices;
    
}ChunkHeader;
''')


raw = loadRaw('1541108087')
header = ffi.new('WorldFileHeader*')
ffi.buffer(header)[:] = raw[:ffi.sizeof('WorldFileHeader')]
print(ffi.string(header.name))
