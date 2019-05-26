#!/bin/bash

if [ -z "$1" ]; then
    echo "ERROR No argument supplied"
    exit 1
fi

gcc -O2 -lm 10$1.c; ./a.out
