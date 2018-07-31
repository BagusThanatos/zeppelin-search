@echo off

if not exist ..\build\settergetter\windows mkdir ..\build\settergetter\windows
pushd ..\build\settergetter\windows
cl -Zi ..\..\..\settergetter\src\cpp\main.cpp -O2
popd