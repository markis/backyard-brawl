#!/bin/bash

mkdir -p $HOME/.ssh

cp /mnt/ssh/* $HOME/.ssh
cp /mnt/config/.gitconfig $HOME/.gitconfig

source /brawl/job.sh
