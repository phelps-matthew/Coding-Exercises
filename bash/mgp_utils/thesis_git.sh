#!/bin/bash
# Shortcut to pushing thesis
cd ~/Cosmological-Perturbations
cp -r ~/Desktop/thesis ~/Cosmological-Perturbations
git add ./thesis
git commit -m 'update thesis'
git push
cd ~


