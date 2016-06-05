#!/bin/sh
sudo aticonfig --adapter=all --initial -f
screen -dmS X xinit
export DISPLAY=:0
sudo aticonfig --odgt --adapter=all
