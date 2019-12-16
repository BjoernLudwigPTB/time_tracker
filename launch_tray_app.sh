#!/bin/bash

# Put here "/your/path/to/repo"
PATH_TO_REPO=~/code/time_tracker

# Put here "/your/path/to/venv" where you would normally do
#
# $ source /your/path/to/venv/bin/activate
PATH_TO_VENV=~/code/envs/time_tracker

# Navigate to the repository folder
cd $PATH_TO_REPO

# This results in executing time_tracker.py inside your virtual environment and
# redirect stdout to /your/path/to/repo/nohup.out, where /your/path/to/repo
# is defined by PATH_TO_REPO in line 4.
nohup $PATH_TO_VENV/bin/python $PATH_TO_REPO/time_tracker.py &
kdialog --passivepopup "Time Tracker is running with PID $!"

