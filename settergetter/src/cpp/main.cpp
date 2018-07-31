#include <stdio.h>
#include <sys/stat.h>

int main(int argc, 
         char *argv[], 
         char *envp[]){
    if(argc < 2) {
        printf("Please specify zeppelin folder as an argument");
        return 0;
    };
    char *path = argv[1];
    
    
    return 0;
};