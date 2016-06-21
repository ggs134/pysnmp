#!/bin/sh
screen -dmS X xinit
export DISPLAY=:0
sudo aticonfig --odgt --adapter=all
