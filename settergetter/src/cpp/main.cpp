#include <stdio.h>
#include <sys/stat.h>

//Check if a directory exist.

struct stat info;

char dirExist(char* dir){
    if( stat( dir, &info ) != 0 ) {
        printf("Can't access directory");
        return 0;
    }
    if( info.st_mode & S_IFDIR ) {
        return 1;
    }
    return 1;
}

int main(int argc, 
         char *argv[], 
         char *envp[]){
    if(argc < 2) {
        printf("Please specify zeppelin folder as an argument");
        return 0;
    };
    char *path = argv[1];
    
    if(dirExist(path)) 
        printf("path exists");
    return 0;
};