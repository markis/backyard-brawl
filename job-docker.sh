#!/bin/bash

mkdir -p $HOME/.ssh

cp /mnt/ssh/* $HOME/.ssh
chmod 600 $HOME/.ssh/*
cp /mnt/config/.gitconfig $HOME/.gitconfig

while true
do
  source /brawl/job.sh
  sleep 300
done
