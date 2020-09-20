#!/bin/bash

source /home/markis/venv/backyard-brawl/bin/activate
python -m brawl

git add .
git commit -m 'Update Score'
git push origin master
