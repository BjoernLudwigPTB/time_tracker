
rem Put here "C:\your\path\to\repo"
set PATH_TO_REPO=%USERPROFILE%/git_repos/time_tracker

rem Put here "C:\your\path\to\venv" where you would normally do
rem
rem $ source /your/path/to/venv/bin/activate
set PATH_TO_VENV=%USERPROFILE%/python_venv/time_tracker

rem Navigate to the repository folder
cd %PATH_TO_REPO%

rem This results in executing time_tracker.py inside your virtual environment and
rem redirect stdout to /your/path/to/repo/nohup.out, where /your/path/to/repo
rem is defined by PATH_TO_REPO in line 4.
%PATH_TO_VENV%\Scripts\python.exe %PATH_TO_REPO%\time_tracker.py
