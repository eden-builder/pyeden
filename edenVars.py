CHUNK_SIZE = 16
CHUNK_SIZE2 = CHUNK_SIZE**2
CHUNK_SIZE3 = CHUNK_SIZE**3

T_SIZE = int((300/CHUNK_SIZE) * CHUNK_SIZE)
T_HEIGHT = int((64/CHUNK_SIZE) * CHUNK_SIZE)

T_BLOCKS = T_SIZE*T_SIZE*T_HEIGHT

CHUNKS_PER_COLUMN = int(T_HEIGHT/CHUNK_SIZE)

SIZEOF_COLUMN = CHUNK_SIZE3 * CHUNKS_PER_COLUMN * 2


fIRST_LAYER = 4096