#!/usr/bin/env bash

# rm *.o
rm output -r

# make

make clean && make;

rm *.o