#!/bin/bash

if [ -d $HOME/venv/backyard-brawl/bin/ ]; then
  source $HOME/venv/backyard-brawl/bin/activate
fi

git pull origin master

python -m brawl

git add data/
git commit -m 'Update Score'
git push origin master
