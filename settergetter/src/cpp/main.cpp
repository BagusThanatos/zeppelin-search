#include <stdio.h>
#include <sys/stat.h>

/*
This is cool!

#define A(x) coba(x)

char coba(int x){
    return x > 5;
};

printf("%d", A(5));
*/

struct stat info;

//Check if directory exists
char dirExist(char* dir){
    if( stat( dir, &info ) != 0 ) {
        printf("Can't access directory");
        return 0;
    }
    if( info.st_mode & S_IFDIR ) {
        return 1;
    }
    return 0;
}

int main(int argc, 
         char *argv[], 
         char *envp[]){
    if(argc < 2) {
        printf("Please specify zeppelin folder as an argument");
        return 0;
    };
    char *path = argv[1];
    
    if(!dirExist(path)) 
        return 0;
    
    return 0;
};