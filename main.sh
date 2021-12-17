#!/bin/bash

cp origin/Lato-Regular.ttf ./

python main.py --dict
echo --------------------------------------------------------------------------------
python fix.py
python main.py --dict

mv Lato-Regular.ttf Crazy-Characters-Regular.ttf
