#!/bin/bash


# ECOSONGS_MAIN="./ecosongs.ui"
# ECOSONGS_MAIN_DEST="../"




# cd gui;

for f in `find . -name "*.ui"`; do
    # echo $f
    # if [[ $f == $ECOSONGS_MAIN ]]; then
    pyside6-uic $f -o $(echo $f | sed s/\\.ui/_ui.py/);
    # fi 
done