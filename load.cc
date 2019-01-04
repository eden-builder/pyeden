#include "stdio.h"


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


int main() {
    FILE *fp = fopen("./1541108087.edenu", "r");
    WorldFileHeader file_header;
    fread(&file_header, sizeof(WorldFileHeader), 1, fp);
    printf("Name: %s\n", file_header.hash);
}