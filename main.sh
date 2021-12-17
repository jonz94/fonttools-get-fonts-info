#!/bin/bash

for file in $(ls ./*.ttf); do
  rm -f $file
done

cp origin/Lato-Regular.ttf ./

python main.py --dict
echo --------------------------------------------------------------------------------
python rename.py
python main.py --dict

rm ./Lato-Regular.ttf
