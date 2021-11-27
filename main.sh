#!/bin/bash

for file in $(ls origin); do
  rm $file
  cp origin/$file ./
done

python main.py --dict
echo --------------------------------------------------------------------------------
python fix.py
python main.py --dict
