#!/bin/bash
# Shortcut to pushing thesis
cd ~/Cosmological-Perturbations
cp -r ~/Desktop/presentation ~/Cosmological-Perturbations/thesis/
git add ./thesis/presentation
git commit -m 'update presentation'
git push
cd ~


