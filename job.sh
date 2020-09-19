#!/bin/bash

docker run -v data:/brawl/data brawl

git add .
git commit -m 'Update Score'
git push origin master
