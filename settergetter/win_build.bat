@echo off

mkdir ..\build\settergetter\windows
pushd ..\build\settergetter\windows
cl -Zi ..\..\settergetter\main.cpp -O2
popd