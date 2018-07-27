rm -rf zeppelin
mkdir -p ../build/settergetter/linux/
clang main.cpp $(< flags_linux.txt) -o ../build/settergetter/linux/main

git clone git@github.com:apache/zeppelin
./build/settergetter/linux/main