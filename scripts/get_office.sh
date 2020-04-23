#!/bin/bash

if [ ! -d "data" ]; then
    mkdir "data"
fi

if [ ! -d "data/Office31" ]; then
    mkdir "data/Office31"
fi


./scripts/gdrivedl.sh "https://drive.google.com/uc?export=download&id=0B4IapRTv9pJ1WGZVd1VDMmhwdlE" tmp.tar.gz  
tar -xvzf tmp.tar.gz -C data/Office31
rm tmp.tar.gz
